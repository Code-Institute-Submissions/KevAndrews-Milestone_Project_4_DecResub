"""
URLs for Cart App
"""
from django.urls import path
from cart.views import Cart

urlpatterns = [
    path('', Cart.as_view(), name='cart'),
]
