"""
Class views for the Home
"""
import random

from django.views import View
from django.shortcuts import render
from products.models import Game


class Index(View):
    """
    Custom Class view for the Home Index page
    """

    def get(self, request):
        """
        Custom GET method for the Home Index page
        """
        games = list(Game.objects.all())

        if bool(games):
            feature_games = random.sample(games, 3)
        else:
            feature_games = list()

        context = {
            'games': feature_games,
            'nav': 'home',
        }

        return render(request, 'home/index.html', context)
