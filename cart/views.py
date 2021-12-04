"""
Class views for the Cart
"""
from django.views import View
from django.shortcuts import render


class Cart(View):
    """
    Class view for the Cart page
    """

    def get(self, request, *args, **kwargs):
        """
        GET method for the Cart page
        """
        return render(request, 'cart/cart.html')
