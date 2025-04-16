from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import get_user_model, logout, authenticate, login
from django.views.decorators.http import require_POST
from restaurant.forms import SignupForm, LoginForm, PaymentForm
from restaurant.models import CustomUser
from .models import MenuItem, CustomUser, UserProfile, Order, OrderItem, GuestOrder  # Import your model
from decimal import Decimal
import random, secrets, string, json
from collections import defaultdict

# Create your views here
def home(request):
    context = {}

    # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user
        messages.info(request, f"Welcome back, {user.first_name}!")  # Personalized greeting
        if hasattr(user, 'role'):  # Ensure 'role' exists
            context['user'] = user
            context['role'] = user.role

            if user.role == 'manager':  # Correct spelling
                context['admin'] = user  # Keeping your logic

    # Fetch four random items from the menu
    random_items = random.sample(list(MenuItem.objects.all()), 4)  # Get 4 random items
    context['random_items'] = random_items

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

# def ordering(request):
#     return render(request, 'ordering.html')

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

# def shopping_cart(request):
#     session_id = request.session.session_key
#     if not session_id:
#         request.session.create()
#         session_id = request.session.session_key
    
#     guest_orders = GuestOrder.objects.filter(session_id=session_id)
#     cart_items = []
    
#     for order in guest_orders:
#         cart_items.append({
#             "item_id": order.item.item_id,
#             "image_url": order.item.image.url if order.item.image else None,
#             "name": order.item.name,
#             "price": order.item.price,
#             "quantity": order.quantity,
#             "subtotal": round(order.item.price * order.quantity, 2)
#         })
    
#     subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
#     delivery_fee = Decimal("5.00")
#     tax = (subtotal + delivery_fee) * Decimal("0.0775")
#     total_price = tax + subtotal
    
#     context = {
#         "cart_items": cart_items,
#         "subtotal": subtotal,
#         "discount": 0,
#         "delivery_fee": delivery_fee,
#         "tax": round(tax, 2),
#         "total_price": round(total_price, 2),
#     }
#     return render(request, 'shopping_cart.html', context)

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

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number'].replace(" ", "")
            card_last4 = card_number[-4:]
            card_name = form.cleaned_data['card_name']

            user = request.user if request.user.is_authenticated else None
            
            def generate_transaction_id(length=16):
                characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
                return ''.join(secrets.choice(characters) for i in range(length))

            # Create the Order first
            order = Order.objects.create(
                customer=user,
                guest_name=card_name if not user else None,
                total_price=total_price,
                card_name=card_name,
                card_last4=card_last4,
                is_paid=True,
                transaction_id=generate_transaction_id(),
                status="processing"
            )

            # Create OrderItems related to the Order
            for guest_item in guest_orders:
                OrderItem.objects.create(
                    order=order,
                    item=guest_item.item,
                    item_name=guest_item.item.name,
                    quantity=guest_item.quantity,
                    price=guest_item.item.price
                )

            # Delete the GuestOrders after creating OrderItems
            guest_orders.delete()
            return redirect('order_success')
    else:
        form = PaymentForm()

    context = {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "discount": 0,
        "delivery_fee": delivery_fee,
        "tax": round(tax, 2),
        "total_price": round(total_price, 2),
        "form": form,
    }
    return render(request, 'shopping_cart.html', context)

# def checkout(request):
    

def order_success(request):
    # Optional: show last 4 digits of the card (if you stored it)
    last4 = request.session.pop('last4', None)

    return render(request, 'order_success.html', {
        'last4': last4
    })
    

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
    
    

# Work in session
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

@require_POST
def update_cart(request):
    try:
        data = json.loads(request.body)
        item_id = data.get("id")
        quantity = int(data.get("quantity", 1))
        session_id = request.session.session_key or request.session.create()

        item = MenuItem.objects.get(pk=item_id)
        order = GuestOrder.objects.get(session_id=request.session.session_key, item=item)

        order.quantity = quantity
        order.save()

        return JsonResponse({"success": True, "updated_quantity": order.quantity})

    except MenuItem.DoesNotExist:
        return JsonResponse({"error": "Item does not exist"}, status=404)
    except GuestOrder.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_POST
def delete_cart_item(request):
    try:
        if not request.session.session_key:
            return JsonResponse({"error": "Session not found"}, status=400)

        data = json.loads(request.body)
        item_id = data.get("id")

        if not item_id:
            return JsonResponse({"error": "Missing item ID"}, status=400)

        item = MenuItem.objects.get(pk=item_id)

        # Only delete the GuestOrder for this session and item
        order = GuestOrder.objects.get(session_id=request.session.session_key, item=item)
        order.delete()

        return JsonResponse({"success": True, "message": "Item removed from cart"})

    except GuestOrder.DoesNotExist:
        return JsonResponse({"error": "Item not in cart"}, status=404)
    except MenuItem.DoesNotExist:
        return JsonResponse({"error": "Item does not exist"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

# Debug test
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

def get_cart_data(request):
    if not request.session.session_key:
        return JsonResponse({"error": "Session not found"}, status=400)

    session_id = request.session.session_key
    cart_items = GuestOrder.objects.filter(session_id=session_id)

    # Group by item_id
    grouped = defaultdict(lambda: {"quantity": 0, "name": "", "image_url": "", "price": 0})
    for order in cart_items:
        item_id = order.item.item_id
        grouped[item_id]["quantity"] += order.quantity
        grouped[item_id]["name"] = order.item.name
        grouped[item_id]["image_url"] = order.item.image.url
        grouped[item_id]["price"] = order.item.price

    data = []
    subtotal = 0

    for item_id, info in grouped.items():
        item_total = info["quantity"] * info["price"]
        subtotal += item_total
        data.append({
            "id": item_id,
            "name": info["name"],
            "quantity": info["quantity"],
            "subtotal": item_total,
            "image_url": info["image_url"],
        })
    delivery_fee = Decimal("5.00")
    tax_rate = Decimal("0.0775")
    tax = (subtotal + delivery_fee) * tax_rate
    total = tax + subtotal + delivery_fee
    return JsonResponse({
        "items": data,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "tax": round(tax , 2),
        "total": round(total, 2)
    })