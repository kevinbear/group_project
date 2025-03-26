from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("Hello World")

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def ordering(request):
    return render(request, 'ordering.html')

def login_signup(request):
    return render(request, 'login_signup.html')