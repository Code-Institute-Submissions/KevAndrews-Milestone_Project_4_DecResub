"""
Class views for the Games / Products
"""
from django.views import View
from django.shortcuts import render
from .models import Game


class AllGames(View):
    """
    Class view for the All Games page
    """

    def get(self, request):
        """
        GET method for the All Games page
        """
        games = Game.objects.all()
        query = None
        categories = None

        context = {
            'games': games,
            'search_term': query,
            'current_categories': categories,
        }

        return render(request, 'products/games.html', context)
