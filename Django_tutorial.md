# Django Tutorial
## Django
Python Web development Framework
+ [django download](https://www.djangoproject.com/download/)
+ [django website](https://docs.djangoproject.com/en/5.1/)

### Install Django
+ Install command macOS/Linux `python -m pip install Django` or `python -m pip install Django==5.12`
+ Install on Windows `py -m pip install Django`

### Django version test
+ `django-admin --version`

### [Django tutorial video](https://www.youtube.com/watch?v=nGIg40xs9e4)
### Create a project
1. Create a new project folder called `django_porject`
2. Use django command to create a default developer structure of folder `django-admin startproject mysite django_project`
3. Understand project directory
   + __init__.py: This file marks the directory as a Python package.
   + asgi.py: ASGI (Asynchronous Server Gateway Interface) is a specification that allows asynchronous web servers to interact with Python web applications. It’s the modern alternative to WSGI (described below).
   + wsgi.py: WSGI (Web Server Gateway Interface) is a standard for Python web applications to communicate with web servers (like Apache or Nginx). This file configures WSGI to allow a web server to interface with Django.
   + settings.py: This is the main configuration file for the Django project. It contains the settings that control how your Django project behaves, such as database configurations, middleware, static files, installed apps, security settings, and much more.
   + urls.py: This file defines the URL routing for your Django project. It maps URLs to views that handle incoming requests and determine what content to return. Django’s URL dispatcher allows you to map web addresses (URLs) to specific views (functions or classes that handle requests).

### Run Server
1. Go to the django_project directory
2. Run command: `python manage.py runserver`
3. Copy url to browser `http://127.0.0.1:8000`

# Start makeing web app
## Create a web app under project
1. Create a web app directory by the command: `python manage.py startapp restaurant`
2. Understand the app directory 
   + admin.py: allow us to register database models
   + models.py place our database models
   + tests.py: some automated test case
   + views.py: we'll create different view or routes
   + urls.py: place different url routes and connect to our view
3. Link to main django project:
   + Open the project direcotry and go to `settings.py` (path: `mysite\settings.py`)
   + Add the app name to `INSTALLED_APPS` list
    ```python
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "restaurant",
    ]
    ```
    + Open `views.py` in restaurant directory (path: `restaurant\views.py`) and add Hello World page
    ```python
    from django.shortcuts import render, HttpResponse
    # Add the HttpResponse
    def test(request):
        return HttpResponse("Hello World")
    ```
    + Create a new files called `urls.py` under the restaurant directory and add the following code to the urls.py
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.test, name='test'),
    ]
    ```
    + Link the test webpage to project `urls.py` (path:`mysite\url.py`)
    ```python
    from django.contrib import admin
    from django.urls import path, include
    # Add the include method

    # Add new restaurant app to the urlpatterns list
    urlpatterns = [
        path('admin/', admin.site.urls),
        path("restaurant/", include('restaurant.urls')),
    ]
    ```
## Create Database

## Use Template
Template is reusable HTML file and it allows us to display dynamic data.

1. Create a folder called `teamplate` (path: `restaurant\template`)