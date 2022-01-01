"""
Views Class for Wishlists
"""
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Game
from profiles.models import UserProfile

from .models import Wishlist


def add_to_wishlist(request, game_id):
    """
    Allow user to add a game to their wishlist
    """
    user = UserProfile.objects.get(user=request.user)
    game = get_object_or_404(Game, pk=game_id)

    wishlist = Wishlist.objects.all()

    wishlist.user = user
    wishlist.save()

    messages.success(request, 'Add to Wishlist')

    return redirect(reverse('game_detail', args=(game_id,)))


def edit_wishlist(request, wishlist_id):
    """
    Allow user to add a game to their wishlist
    """
    messages.success(request, 'Edit Wishlist')


def delete_wishlist(request, wishlist_id):
    """
    Allow user to add a game to their wishlist
    """
    messages.success(request, 'Delete Wishlist')
