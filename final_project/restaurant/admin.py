from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, UserProfile, MenuItem, Order
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'role', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_superuser', 'is_active'),
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
    list_display = ('item_id', 'name', 'price', 'category', 'combo_price', 'image_preview')  # Add image_preview here
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('category', 'name',)

    fieldsets = (
        (None, {'fields': ('name', 'price', 'category', 'combo_price', 'image')}),  # No duplicates
    )
    
    def image_preview(self, obj):
        """Display image preview in the admin panel."""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'total_price', 'status', 'order_date')
    search_fields = ('user__email',)
    list_filter = ('status',)
    ordering = ('-order_date',)