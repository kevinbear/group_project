from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from restaurant.forms import SignupForm
from restaurant.models import CustomUser

# Create your views here.ß

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def ordering(request):
    return render(request, 'ordering.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to the login page or another page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def custom_404(request, exception):
    return render(request, '404.html', status=404)