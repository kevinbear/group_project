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

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     # Customize the list display to include transaction_id and other relevant fields
#     list_display = (
#         'order_id', 'customer', 'item', 'quantity', 
#         'total_price', 'status', 'is_paid', 
#         'card_name', 'card_last4', 'transaction_id', 'order_date',
#     )
    
#     # Add search functionality for transaction_id and other fields
#     search_fields = ('customer__email', 'transaction_id', 'card_name')
    
#     # Filters for status and whether the order is paid
#     list_filter = ('status', 'is_paid')
    
#     # Default ordering by order_date
#     ordering = ('-order_date',)
    
#     # Define the fieldsets to organize the order details in the form view
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'customer', 'item', 'quantity', 'total_price',
#                 'status', 'is_paid', 'transaction_id', 'card_name',
#                 'card_last4', 'order_date',
#             )
#         }),
#     )

#     # Optionally, you can add custom actions like marking orders as shipped
#     actions = ['mark_as_shipped']

#     def mark_as_shipped(self, request, queryset):
#         queryset.update(status='shipped')
#     mark_as_shipped.short_description = "Mark selected orders as shipped"

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