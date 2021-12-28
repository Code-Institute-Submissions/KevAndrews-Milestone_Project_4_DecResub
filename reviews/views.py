from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Game
from profiles.models import UserProfile


def add_review(request, game_id):
    """
    Allow user to add a review and redirect them back to the
    item game item view
    """
    user = UserProfile.objects.get(user=request.user)
    game = get_object_or_404(Game, pk=game_id)
    review_form = ReviewForm()
    review_details = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }
    review_form = ReviewForm(review_details)

    # If form is valid, add user and game and save
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.game = game
        review.save()

        reviews = Review.objects.filter(game=game)

        game.save()

        messages.success(request, 'Thank you! Your review was added')
    else:
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('game_detail', args=(game_id,)))


def edit_review(request, review_id):
    """
    Saves review form edited by user
    """
    review = get_object_or_404(Review, pk=review_id)
    review_form = ReviewForm(request.POST, instance=review)
    game = Game.objects.get(name=review.game)
    if review_form.is_valid():
        review.save()

        reviews = Review.objects.filter(game=game)

        game.save()

        # Success message if added
        messages.success(request, 'Thank You! Your review was edited')
    else:
        # Error message if form was invalid
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('game_detail', args=(review.game.id,)))


def delete_review(request, review_id):
    """
    Deletes user's review
    """
    review = get_object_or_404(Review, pk=review_id)
    game = Game.objects.get(name=review.game)

    try:
        review.delete()

        reviews = Review.objects.filter(game=game)

        game.save()
        messages.success(request, 'Your review was deleted')

    # If deletion failed, return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" eroor:{e} occured. Try again later.")

    return redirect(reverse('game_detail', args=(review.game.id,)))
