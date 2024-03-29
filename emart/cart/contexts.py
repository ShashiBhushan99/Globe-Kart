from django.shortcuts import get_object_or_404
from product.models import product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page. 
    """

    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product1 = get_object_or_404(product, pk=id)
        total += quantity * int(product1.Total)
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product1})

    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }