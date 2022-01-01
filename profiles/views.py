"""
Class Views for rhw Profile page
"""

from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.contrib import messages
from django.views import View
from checkout.models import Order
from wishlists.models import Wishlist
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

        wishlist = Wishlist.objects.all()

        context = {
            'form': form,
            'orders': orders,
            'wishlist': wishlist,
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

        # Custom Code to remove Profiles
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


class OrderHistory(View):
    """
    Class for the Order History.
    """

    def get(self, request, order_number):
        """
        Display the user's order history.
        Custom Code
        """
        order = get_object_or_404(Order, order_number=order_number)

        # Custom Code Get Current User
        profile_user = get_object_or_404(UserProfile, user=request.user)

        # Check if Order User id is equal to Current User id
        # If True load order, else redirect back to Profile
        if (order.user_profile.id == profile_user.id or
                request.user.is_superuser):

            if request.user.is_superuser:
                messages.info(request, (
                    f'This is a past confirmation for order number\
                        {order_number}. This order belongs to\
                            {order.user_profile}.'
                ))
            else:
                messages.info(request, (
                    f'This is a past confirmation for order number\
                        {order_number}. A confirmation email was\
                            sent on the order date.'
                ))

            context = {
                'order': order,
                'from_profile': True,
            }

            return render(request, 'checkout/checkout_success.html', context)
        else:
            messages.info(request, (
                'Current User does not have permission to view this order'
            ))
            return redirect(reverse('profile'))

        # If we reach here something has gone wrong
        return redirect(reverse('profile'))
