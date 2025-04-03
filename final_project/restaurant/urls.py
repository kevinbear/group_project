from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup, logout_view, login_view

urlpatterns = [
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('home', views.home, name='home'),
    path('ordering', views.ordering, name='ordering'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('checkout', views.checkout, name='checkout'),
    # path('signup', views.signup, name='signup'),
    # path('signup/', auth_views.LoginView.as_view(template_name='siguup.html'), name='signup'),
    path('signup/', signup, name='signup'),
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
]