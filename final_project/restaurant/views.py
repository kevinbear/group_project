from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import get_user_model, logout, authenticate, login
from restaurant.forms import SignupForm, LoginForm
from restaurant.models import CustomUser
from .models import MenuItem, CustomUser, UserProfile, Order  # Import your model
# Create your views here

def home(request):
    context = {}  # Create an empty context dictionary
    if request.user.is_authenticated:
        user = request.user
        messages.info(request, f"Welcome back, {user.first_name}!")  # Use first_name for a more personal touch
        if hasattr(user, 'role'):  # Ensure 'role' exists
            context['user'] = user
            context['role'] = user.role

            if user.role == 'manager':  # Correct spelling
                context['admin'] = user  # Keeping your logic

    return render(request, 'home.html', context)

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f"Welcome {user.first_name}, login successful!")
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid email or password.")
    
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                print("DEBUG: Form is valid")  # Debugging print
                # Create user using CustomUser model
                User = get_user_model()
                user = User.objects.create_user(
                    email=form.cleaned_data['email'],  # Use email as the username
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password']
                )
                print(f"DEBUG: User {user.email} created successfully")  # Debugging print
                messages.success(request, "Account created successfully!")
                return redirect('login')  # Redirect to login page
            except Exception as e:
                print(f"DEBUG: Error creating user - {e}")  # Debugging print
                messages.error(request, f"Error creating user: {e}")
        else:
            print("DEBUG: Form is NOT valid")  # Debugging print
            print("DEBUG: Form errors:", form.errors)  # Show form errors in console
            messages.error(request, "There was an error with your form.")

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def shopping_cart(request):
    return render(request, 'shopping_cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirect after logout

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = {} # user.profile  # Assuming you have a OneToOne relationship with UserProfile
        return render(request, 'user_profile.html', {'profile': profile})
    else:
        messages.error(request, "You need to be logged in to view this page.")
        return redirect('login')