from .models import Category
from .models import CartItem, WishlistItem


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def cart_and_wishlist_counts(request):
    cart = request.session.get('cart', {})
    wishlist_count = WishlistItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    cart_count = sum(item['quantity'] for item in cart.values()) if cart else 0
    return {'cart_item_count': cart_count, 'wishlist_item_count': wishlist_count}