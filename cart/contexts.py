"""
Context for the Carts content
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Game


def cart_contents(request):
    """
    Context for the Carts content
    Code taken from Boutique Ado project
    Modified to work with this project
    """
    cart_items = []
    total = 0
    game_count = 0
    cart = request.session.get('cart', {})

    for game_id, game_data in cart.items():
        if isinstance(game_data, int):
            game = get_object_or_404(Game, pk=game_id)
            total += game_data * game.price
            game_count += game_data
            cart_items.append({
                'game_id': game_id,
                'quantity': game_data,
                'game': game,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'game_count': game_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
