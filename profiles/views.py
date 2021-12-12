"""
Class Views for rhw Profile page
"""

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import View
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


class Profile(View):
    """
    Class for the user's profile.
    """

    def get(self, request):
        """
        GET Method for the user's profile.
        Used Boutique Ado project for logic and updated it
        to work in this project
        """
        profile_user = get_object_or_404(UserProfile, user=request.user)

        form = UserProfileForm(instance=profile_user)
        orders = profile_user.orders.all()

        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

        return render(request, 'profiles/profile.html', context)

    def post(self, request):
        """
        POST method for the user's profile.
        Used Boutique Ado project for logic and updated it
        to work in this project
        """
        profile_user = get_object_or_404(UserProfile, user=request.user)

        form = UserProfileForm(request.POST, instance=profile_user)

        if 'delete_profile' in request.POST:
            request.user.delete()
            request.session.delete()
            messages.success(request, 'Profile deleted successfully')
            return render(request, 'home/index.html')

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
            )

        form = UserProfileForm(instance=profile_user)
        orders = profile_user.orders.all()

        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

        return render(request, 'profiles/profile.html', context)

    def order_history(self, request, order_number):
        """
        Display the user's order history.
        """
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent on the order date.'
        ))

        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, 'checkout/checkout_success.html', context)
