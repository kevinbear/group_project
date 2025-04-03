from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from restaurant.forms import SignupForm
from restaurant.models import CustomUser
from .models import MenuItem, CustomUser, UserProfile, Order  # Import your model
# Create your views here.ß

def home(request):
    return render(request, 'home.html')

def menu(request):
    breakfast_items = MenuItem.objects.filter(category='breakfast')
    lunch_items = MenuItem.objects.filter(category='lunch')
    dinner_items = MenuItem.objects.filter(category='dinner')

    return render(request, 'menu.html', {
        'breakfast_items': breakfast_items,
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
    })

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

def shopping_cart(request):
    return render(request, 'shopping_cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)