from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('home', views.home, name='home'),
    path('ordering', views.ordering, name='ordering'),
    path('login_signup', views.login_signup, name='login_signup'),
]