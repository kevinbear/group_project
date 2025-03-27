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

1. Create a folder called `teamplates` (path: `restaurant\templates`)
2. Add the HTML files
### Reuse base.html
1. Create a `base.html`
2. Put the reusable component to base.html
```html
{% load static%}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=f, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    <link href="{% static 'css/base.css'%}" rel="stylesheet" />
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
    <title>Restaurant Web App</title>
  </head>
  <body>
    <!-- Header -->
    <header class="py-3 bg-light" id="header_section">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
          <a class="navbar-brand ps-5" href="{%url 'home'%}"
            ><b class="h3">Restaurant Web App</b></a
          >
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="text-center nav-item">
              <a class="nav-link active" href="{% url 'menu'%}">Menu</a>
            </li>
            <li class="text-center nav-item">
              <a class="nav-link active" href="{% url 'ordering'%}">Order</a>
            </li>
            <li class="text-center nav-item">
              <a class="nav-link active" href="{% url 'about'%}">About</a>
            </li>
            <button class="btn btn-primary me-5 ms-5" type="button">
              <a
                class="text-white text-decoration-none"
                href="{% url 'login_signup' %}"
                >Login</a
              >
            </button>
          </ul>
        </div>
      </nav>
    </header>
    <!-- Different Main for different pages -->
    <main>{%block placeholder%} Base HTML {%endblock%}</main>
    <!-- Footer -->
    <footer id="footer_bg" class="mt-5">
      <div>
        <p class="m-0">Restaurant Web App &copy; 2025</p>
      </div>
    </footer>
  </body>
</html>
```
3. Put the `{%block placeholder%}` and `{%endblock%}` to the `base.html`. The syntax of `{%block content%}` and `{%endblock%}` is for other HTML file can place other content into the `base.html`.
4. Create differnt HTML files into `templates` folder:
    + about.html
    + home.html
    + login_signup.html
    + menu.html
    + ordering.html
5. In the each HTML file, we can use `{% extends "base.html" %}` on first line and put `{%block placeholder%}` `{%block%}`to the following line. After we put specific HTML components in between `{%block placeholder%}` `{%block%}`, the django will insert our HTML components to the template. When server send process HTMl file to the client will be a whole and finished HTML file. By using base.html template, we don't need to copy paste the same element in each HTML file.

### Static Files
1. Static files includes `css`, `image`, and `js` files
2. We will put the iamge and set up stylesheet for our HTML, so it is important to create a static folder to store those files. For our project, I put the `static` folder under `restaurant` application folder
3. Next, go to the `mysite/settings.py` to add following line
    ```python
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        BASE_DIR / "restaurant" / "static",
    ]
    ```
4. Add the `{% load static %}` to HTML file which use the static files
5. The syntax of the static file `{% static 'css/yourStyleSheet.css' %}` or `{% static 'image/yourImage.jpg'%}`. The path is following your static directory. If you put everything to static folder and without categorizing them you can just put the files name. Eg. `{% static 'image/yourImage.jpg'%}`