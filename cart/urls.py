"""
URLs for Cart App
"""
from django.urls import path
from cart.views import Cart, AddToCart, UpdateCart, RemoveFromCart

urlpatterns = [
    path('', Cart.as_view(), name='cart'),
    path('add/<game_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('update/<game_id>/', UpdateCart.as_view(), name='update_cart'),
    path('remove/<game_id>/', RemoveFromCart.as_view(), name='remove_from_cart'),
]
