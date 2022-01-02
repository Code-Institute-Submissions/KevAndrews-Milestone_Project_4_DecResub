"""
URLs for the Wishlists App
"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('add_to_wishlist/<int:game_id>',
         login_required(views.add_to_wishlist), name="add_to_wishlist"),
    path('delete_from_wishlist/<int:game_id>',
         login_required(views.delete_from_wishlist), name="delete_from_wishlist"),
]
