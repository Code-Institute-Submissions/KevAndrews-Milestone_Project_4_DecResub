"""
URLs for the Wishlists App
"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('create_wishlist/',
         login_required(views.create_wishlist), name="create_wishlist"),
    path('add_to_wishlist/<int:game_id>',
         login_required(views.add_to_wishlist), name="add_to_wishlist"),
    path('edit_wishlist/<wishlist_id>',
         login_required(views.edit_wishlist), name="edit_wishlist"),
    path('delete_wishlist/<wishlist_id>',
         login_required(views.delete_wishlist), name="delete_wishlist"),
]
