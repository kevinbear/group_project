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
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,  # Apply the choices to the category field
        default='breakfast'  # Set a default category if needed
    )
    
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Image field to store product images
    combo_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional combo price
    def __str__(self):
        return f"{self.name} - ${self.price} ({self.get_category_display()})"  # This should work

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True) # Automatically set the date when the order is created
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # Total price of the order
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Order status
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"