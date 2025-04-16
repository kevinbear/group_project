from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup, logout_view, login_view


urlpatterns = [
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('order_success/', views.order_success, name='order_success'),
    path('signup/', signup, name='signup'),
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
    path('show-cart/', views.show_cart, name="show_cart"),
    path('update-cart/', views.update_cart, name="update_cart"),
    path('delete-cart-item/', views.delete_cart_item, name="delete_cart_item"),
    path('get-cart-data/', views.get_cart_data, name="get_cart_data"),
]