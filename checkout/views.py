"""
Class views for the Checkout
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import View

from .forms import OrderForm


class Checkout(View):
    """
    Custom Class view for the Checkout page
    """

    def get(self, request):
        """
        GET method for the Checkout page
        Used Boutique Ado project for logic and updated it
        to work in this project
        """
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        order_form = OrderForm()

        context = {
            'order_form': order_form,
        }

        return render(request, 'checkout/checkout.html', context)
