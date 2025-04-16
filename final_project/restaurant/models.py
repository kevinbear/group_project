from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now  # Import timezone.now

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'manager') # Default role for superuser

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('manager', 'Manager'),
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')  # Role field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier for login
    REQUIRED_FIELDS = []  # No additional fields required

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"

class MenuItem(models.Model) :
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)  # Optional description field
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,  # Apply the choices to the category field
        default='breakfast'  # Set a default category if needed
    )
    
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Image field to store product images
    # image = models.ImageField(upload_to='menu_images/', blank=False, null=False)
    combo_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional combo price
    def __str__(self):
        return f"{self.name} - ${self.price} ({self.get_category_display()})"  # This should work
    
class GuestOrder(models.Model):
    session_id = models.CharField(max_length=100)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]

#     order_id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
#     guest_name = models.CharField(max_length=100, blank=True, null=True)
#     item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="orders")
#     quantity = models.PositiveIntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     card_name = models.CharField(max_length=100, blank=True, null=True)
#     card_last4 = models.CharField(max_length=4, blank=True, null=True)
#     is_paid = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, blank=True, null=True) 

#     # Simplified: no choice, just assume it's a card
#     is_paid = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         # Safely access customer email or fallback to guest_name
#         return self.customer.email if self.customer else self.guest_name or "Guest"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    is_paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    card_last4 = models.CharField(max_length=4, null=True, blank=True)
    card_name = models.CharField(max_length=100, null=True, blank=True)
    guest_name = models.CharField(max_length=100, null=True, blank=True)
    customer = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.email if self.customer else self.guest_name}"

# class Order(models.Model):
#     guest_name = models.CharField(max_length=255)
#     card_name = models.CharField(max_length=255)
#     card_last4 = models.CharField(max_length=4)
#     order_id = models.CharField(max_length=20, unique=True)
#     customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(auto_now_add=True)
#     is_paid = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=255, blank=True, null=True)  # Optional for payment systems

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per item

    def __str__(self):
        return f"{self.quantity} x {self.item_name}"
    
