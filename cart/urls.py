"""
URLs for Cart App
"""
from django.urls import path
from cart.views import Cart, CartAction

urlpatterns = [
    path('', Cart.as_view(), name='cart'),
    path('add/<game_id>/', CartAction.as_view(), name='add_to_cart'),
]
