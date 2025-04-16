from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, UserProfile, MenuItem, Order, OrderItem, GuestOrder
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'first_name', 'last_name')
    search_fields = ('email','first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Personal Info', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'role', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )
    
    # Separate superusers and customers in the admin
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Superusers see all users
        return queryset.filter(role='customer')  # Non-superusers see only customers

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'date_of_birth')
    search_fields = ('user__email',)
    
# Register the MenuItem model
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'name', 'price', 'category', 'combo_price', 'image_preview', 'description')  # Add image_preview here
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('category', 'name',)

    fieldsets = (
        (None, {'fields': ('name', 'price', 'category', 'combo_price', 'image', 'description')}),  # No duplicates
    )
    
    def image_preview(self, obj):
        """Display image preview in the admin panel."""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

# Inline class for OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display by default

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item_name', 'quantity', 'price')
    search_fields = ('order__order_id', 'item_name')
    list_filter = ('order',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'total_price', 'status', 'is_paid', 'transaction_id', 'order_date')
    search_fields = ('order_id', 'customer__email', 'transaction_id')
    list_filter = ('status', 'is_paid')
    ordering = ('-order_date',)
    readonly_fields = ('order_date',) 

    fieldsets = (
        (None, {
            'fields': ('customer', 'status', 'total_price', 'is_paid', 'transaction_id', 'order_date')
        }),
    )
    inlines = [OrderItemInline]

# Register the GuestOrder model
@admin.register(GuestOrder)
class GuestOrderAdmin(admin.ModelAdmin):
    list_display = ("session_id", "item", "quantity", "added_at")
    search_fields = ("session_id", "item__name")
    list_filter = ("added_at",)