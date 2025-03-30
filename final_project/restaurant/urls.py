from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('home', views.home, name='home'),
    path('ordering', views.ordering, name='ordering'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]