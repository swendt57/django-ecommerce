from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """Allows the cart to be displayed anywhere in the app"""

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for identifier, quantity in cart.items():
        product = get_object_or_404(Product, pk=identifier)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': identifier, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}