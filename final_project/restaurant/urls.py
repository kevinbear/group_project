from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('home', views.home, name='home'),
    path('ordering', views.ordering, name='ordering'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]