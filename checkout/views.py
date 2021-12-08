"""
Class views for the Checkout
"""

import json
import stripe

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import View
from django.conf import settings

from cart.contexts import cart_contents
from products.models import Game
from .forms import OrderForm
from .models import Order, OrderLineItem


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
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret
        }

        return render(request, 'checkout/checkout.html', context)

    def post(self, request):
        """
        POST method for the Checkout page
        Used Boutique Ado project for logic and updated it
        to work in this project
        """
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)     
            order.original_bag = json.dumps(cart)
            order.save()

            for item_id, item_data in cart.items():
                try:
                    game = Game.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        game=game,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Game.DoesNotExist:
                    messages.error(request, (
                        "One of the games in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': stripe_secret_key
        }

        return render(request, 'checkout/checkout.html', context)


class CheckoutSuccess(View):
    """
    Custom Class view for the Checkout Success page
    """

    def get(self, request, order_number):
        """
        GET method for the Checkout Success page
        Used Boutique Ado project for logic and updated it
        to work in this project
        """

        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)

        messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

        if 'cart' in request.session:
            del request.session['cart']

        context = {
            'order': order,
        }

        return render(request, 'checkout/checkout_success.html', context)
