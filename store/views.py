from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product, Category, CartItem, WishlistItem
from .forms import ProductForm, CategoryForm

# ============================
# 🏠 FRONTEND VIEWS
# ============================

def index(request):
    products = Product.objects.all()
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id and category_id.isdigit():
        products = products.filter(category_id=int(category_id))

    paginator = Paginator(products, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'store/index.html', {
        'products': page_obj,
        'query': query,
        'selected_category': int(category_id) if category_id and category_id.isdigit() else None,
        'page_obj': page_obj,
        'categories': Category.objects.all(),
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


# ============================
# 🛒 CART VIEWS
# ============================

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})

    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1
    else:
        cart[str(pk)] = {'quantity': 1, 'price': float(product.price)}

    request.session['cart'] = cart
    request.session.modified = True
    messages.success(request, f"✅ {product.name} added to cart!")

    return redirect('store:cart')


@login_required
def cart(request):
    cart_session = request.session.get('cart', {})
    cart_items = []
    total = 0

    for pk, item in cart_session.items():
        product = get_object_or_404(Product, pk=pk)
        quantity = item.get('quantity', 1)
        total += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def update_cart(request, pk):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        if str(pk) in cart:
            if action == 'increase':
                cart[str(pk)]['quantity'] += 1
            elif action == 'decrease':
                cart[str(pk)]['quantity'] -= 1
                if cart[str(pk)]['quantity'] <= 0:
                    del cart[str(pk)]
            request.session['cart'] = cart
            request.session.modified = True
            messages.success(request, "Cart updated successfully ✅")

    return redirect('store:cart')


@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
        request.session.modified = True
        messages.info(request, "Removed from cart ❌")
    return redirect('store:cart')


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, item in cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            product.quantity = item['quantity']
            products.append(product)
            total += product.price * item['quantity']
        except Product.DoesNotExist:
            continue

    if request.method == 'POST':
        # For demo, we just show a success message
        messages.success(request, "✅ Payment done! Thank you for your purchase.")
        # Optionally, clear the cart or remove selected items
        # request.session['cart'] = {}  # uncomment to clear cart
        return redirect('store:checkout')  # stay on checkout page

    return render(request, 'store/checkout.html', {
        'products': products,
        'total': total
    })

@login_required
def checkout_selected(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_items')  # Get selected checkboxes
        cart = request.session.get('cart', {})
        selected_products = []
        total = 0

        # Check if any product was selected
        if not selected_ids:
            messages.warning(request, "⚠️ Please select at least one product to checkout.")
            return redirect('store:cart')

        for product_id in selected_ids:
            if product_id in cart:
                try:
                    product = Product.objects.get(pk=product_id)
                    quantity = cart[product_id]['quantity']
                    selected_products.append({
                        'product': product,
                        'quantity': quantity,
                        'total': product.price * quantity
                    })
                    total += product.price * quantity
                except Product.DoesNotExist:
                    continue

        # Render checkout page with selected items
        return render(request, 'store/checkout.html', {
            'products': [item['product'] for item in selected_products],
            'selected_items': selected_products,
            'total': total,
            'selected_checkout': True
        })
    else:
        return redirect('store:cart')



# ============================
# 💖 WISHLIST VIEWS
# ============================

@login_required
def wishlist(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'wishlist_items': items})


@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)

    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'added_at': timezone.now()}
    )

    if created:
        messages.success(request, f"💖 {product.name} added to your wishlist!")
    else:
        wishlist_item.delete()
        messages.info(request, f"{product.name} removed from your wishlist ❌")

    return redirect(request.META.get('HTTP_REFERER', 'store:index'))


@login_required
def remove_from_wishlist(request, pk):
    item = get_object_or_404(WishlistItem, pk=pk, user=request.user)
    item.delete()
    messages.info(request, "Removed from wishlist ❌")
    return redirect('store:wishlist')


# ============================
# NAVBAR CONTEXT PROCESSOR
# ============================

def cart_and_wishlist_counts(request):
    cart = request.session.get('cart', {})
    wishlist_count = WishlistItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    cart_count = sum(item['quantity'] for item in cart.values())
    return {'cart_item_count': cart_count, 'wishlist_item_count': wishlist_count}


# ============================
# AUTHENTICATION
# ============================

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')  # Redirect back after login
            return redirect(next_url or 'store:index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'store/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('store:register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('store:register')
        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "✅ Registration successful! Please log in.")
        return redirect('store:login')
    return render(request, 'store/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, "👋 You have been logged out successfully.")
    return redirect('store:index')


# ============================
# ADMIN DASHBOARD & CRUD
# ============================

# Admin check decorator
admin_required = user_passes_test(lambda u: u.is_superuser)

@admin_required
def admin_dashboard(request):
    return render(request, 'store/admin/dashboard.html')


# ===== PRODUCTS CRUD =====
@admin_required
def product_list(request):
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 10)  # 5 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/admin/product_list.html', {'page_obj': page_obj})

@admin_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Product created successfully!")
        return redirect('store:product_list')
    return render(request, 'store/admin/product_form.html', {'form': form})

@admin_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully!")
        return redirect('store:product_list')
    return render(request, 'store/admin/product_form.html', {'form': form, 'product': product})

@admin_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.info(request, "Product deleted successfully!")
    return redirect('store:product_list')


# ===== CATEGORIES CRUD =====
@admin_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/admin/category_list.html', {'categories': categories})

@admin_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Category created successfully!")
        return redirect('store:category_list')
    return render(request, 'store/admin/category_form.html', {'form': form})

@admin_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Category updated successfully!")
        return redirect('store:category_list')
    return render(request, 'store/admin/category_form.html', {'form': form, 'category': category})

@admin_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.info(request, "Category deleted successfully!")
    return redirect('store:category_list')
