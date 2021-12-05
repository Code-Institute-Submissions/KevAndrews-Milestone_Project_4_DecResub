"""
Class views for the Home
"""
from django.views import View
from django.shortcuts import render
from products.models import Game
import random


class Index(View):
    """
    Custom Class view for the Home Index page
    """

    def get(self, request, *args, **kwargs):
        """
        Custom GET method for the Home Index page
        """
        games = list(Game.objects.all())

        feature_games = random.sample(games, 3)

        context = {
            'games': feature_games
        }

        return render(request, 'home/index.html', context)
