"""
Views Class for Wishlists
"""
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Game
from profiles.models import UserProfile

from .models import Wishlist
from .forms import WishlistForm


def create_wishlist(request):

    wishlist_form = WishlistForm()

    user = UserProfile.objects.get(user=request.user)

    wishlist = wishlist_form.save(commit=False)
    wishlist.user = user
    wishlist.save()

    messages.success(request, 'Valid')

    return redirect(reverse('profile'))


def add_to_wishlist(request, game_id):
    """
    Allow user to add a game to their wishlist
    """
    user = UserProfile.objects.get(user=request.user)

    check_wishlist = Wishlist.objects.filter(user=user).exists()

    if check_wishlist:
        wishlist = Wishlist.objects.get(user=user)

        if wishlist.game_ids:
            list_of_games = wishlist.game_ids.split(',')

            if not str(game_id) in list_of_games:
                wishlist.game_ids += f',{game_id}'

                # Check if the Wishlist already exists and updated or create
                wishlist = Wishlist.objects.update_or_create(
                    user=user, defaults={"game_ids": wishlist.game_ids}
                )

                messages.success(request, 'Added Game to your Wishlist')
            else:
                messages.success(request, 'Game is already in your list')
    else:
        # Check if the Wishlist already exists and updated or create
        Wishlist.objects.update_or_create(
            user=user, defaults={"title": 'Get new title', "game_ids": game_id}
        )

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
