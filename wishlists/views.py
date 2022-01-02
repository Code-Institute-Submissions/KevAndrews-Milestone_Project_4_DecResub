"""
Views Class for Wishlists
"""
from django.shortcuts import redirect, reverse
from django.contrib import messages

from profiles.models import UserProfile

from .models import Wishlist


def add_to_wishlist(request, game_id):
    """
    Allow user to add a game to their wishlist
    """
    user = UserProfile.objects.get(user=request.user)

    # Check if a wishlist for the given user exists
    check_wishlist = Wishlist.objects.filter(user=user).exists()

    if check_wishlist:
        # Get the wishlist for the user
        wishlist = Wishlist.objects.get(user=user)

        # Check if the wishlist is empty
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
                messages.success(request, 'Game is already in your Wishlist')
    else:
        # If Check fails create and add selected game
        # Check if the Wishlist already exists and updated or create
        Wishlist.objects.update_or_create(
            user=user, defaults={"game_ids": game_id}
        )

        messages.success(request, 'Added Game to your Wishlist')

    return redirect(reverse('game_detail', args=(game_id,)))


def delete_from_wishlist(request, game_id):
    """
    Allow user to add a game to their wishlist
    """
    user = UserProfile.objects.get(user=request.user)

    # Check if a wishlist for the given user exists
    check_wishlist = Wishlist.objects.filter(user=user).exists()

    if check_wishlist:
        # Get the wishlist for the user
        wishlist = Wishlist.objects.get(user=user)

        # Check if the wishlist is empty
        if wishlist.game_ids:
            list_of_games = wishlist.game_ids.split(',')

            if str(game_id) in list_of_games:
                list_of_games.remove(str(game_id))

                wishlist.game_ids = ','.join(map(str, list_of_games))

                print(wishlist.game_ids)

                # Check if the Wishlist already exists and updated or create
                wishlist = Wishlist.objects.update_or_create(
                    user=user, defaults={"game_ids": wishlist.game_ids}
                )

                messages.success(request, 'Selected game has been removed from Wishlist')

    return redirect(reverse('profile'))
