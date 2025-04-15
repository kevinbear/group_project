from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import get_user_model, logout, authenticate, login
from django.views.decorators.http import require_POST
from restaurant.forms import SignupForm, LoginForm
from restaurant.models import CustomUser
from .models import MenuItem, CustomUser, UserProfile, Order, GuestOrder  # Import your model
import json
from decimal import Decimal
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

    return render(request, 'menu_new.html', {
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
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key
    
    guest_orders = GuestOrder.objects.filter(session_id=session_id)
    cart_items = []
    
    for order in guest_orders:
        cart_items.append({
            "item_id": order.item.item_id,
            "image_url": order.item.image.url if order.item.image else None,
            "name": order.item.name,
            "price": order.item.price,
            "quantity": order.quantity,
            "subtotal": round(order.item.price * order.quantity, 2)
        })
    
    subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    delivery_fee = Decimal("5.00")
    tax = (subtotal + delivery_fee) * Decimal("0.0775")
    total_price = tax + subtotal
    
    context = {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "discount": 0,
        "delivery_fee": delivery_fee,
        "tax": round(tax, 2),
        "total_price": round(total_price, 2),
    }
    return render(request, 'shopping_cart.html', context)

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
    
    
# Work with session
# def add_to_cart(request):
    
#     if request.method == "POST":
#         data = json.loads(request.body)
#         item_id = str(data.get("id"))
#         item_name = data.get("name")
#         item_price = data.get("price")

#         cart = request.session.get("cart", {})

#         if item_id in cart:
#             cart[item_id]["quantity"] += 1
#         else:
#             cart[item_id] = {
#                 "name": item_name,
#                 "price": item_price,
#                 "quantity": 1
#             }

#         request.session["cart"] = cart
#         return JsonResponse({"status": "ok", "cart": cart})
    
@require_POST
def add_to_cart(request):
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key

    try:
        # Parse JSON body from fetch
        data = json.loads(request.body)
        item_id = data.get("id")
        quantity = int(data.get("quantity", 1))  # default to 1

        print(f"Received item_id: {item_id}, quantity: {quantity}")

        # Check if item_id is valid
        if not item_id:
            return JsonResponse({"error": "Missing item ID"}, status=400)

        item = MenuItem.objects.get(pk=item_id)

        # Check if the item already exists in cart
        existing_order = GuestOrder.objects.filter(session_id=session_id, item=item).first()

        if existing_order:
            existing_order.quantity += quantity
            existing_order.save()
        else:
            GuestOrder.objects.create(session_id=session_id, item=item, quantity=quantity)

        return JsonResponse({"success": True, "item": item.name, "quantity": quantity})

    except MenuItem.DoesNotExist:
        return JsonResponse({"error": "Item does not exist."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def show_cart(request):
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key

    guest_orders = GuestOrder.objects.filter(session_id=session_id)

    cart_items = []
    for order in guest_orders:
        cart_items.append({
            "item_id": order.item.item_id,
            "name": order.item.name,
            "price": order.item.price,
            "quantity": order.quantity,
            "subtotal": round(order.item.price * order.quantity, 2)
        })

    return JsonResponse({"cart": cart_items})