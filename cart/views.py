"""
Class views for the Cart
"""
from django.views import View
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Game


class Cart(View):
    """
    Custom Class view for the Cart page
    """

    def get(self, request):
        """
        Custom GET method for the Cart page
        """
        return render(request, 'cart/cart.html')


class CartAction(View):
    """
    Custom Class to handle the requests for
    Cart actions Get and Post to the Cart
    """

    def post(self, request, game_id):
        """
        POST method to Add game / product to Cart
        Code taken from Boutique Ado project
        Modified to work with this project
        """
        game = get_object_or_404(Game, pk=game_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')

        cart = request.session.get('cart', {})

        if game_id in list(cart.keys()):
            cart[game_id] += quantity
            messages.success(
                request, f'Updated {game.name} quantity to {cart[game_id]}')
        else:
            cart[game_id] = quantity
            messages.success(request, f'Added {game.name} to your bag')

        request.session['cart'] = cart
        return redirect(redirect_url)
