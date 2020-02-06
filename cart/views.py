from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """Renders the cart contents page"""
    return render(request, 'cart.html')
    # don't have top pass in a dictionary of contents because cart is available everywhere in the app. It was registerd
    # in settings.py in TEMPLATES>OPTIONS> content_processors


def add_to_cart(request, id):
    """Adds the quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjusts the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# def test_quantity(request):
#     if request.POST.get('quantity').isdigit():
#         return int(request.POST.get('quantity'))
#     else:
#         return 0  # is not correct for adjust function
