"""
Class views for the Games / Products
"""
from django.views import View
from django.shortcuts import render, get_object_or_404
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


class GameDetail(View):
    """
    Class view for a Game's details
    """

    def get(self, request, game_id):
        """
        GET method for Game's details page
        """
        game = get_object_or_404(Game, pk=game_id)

        context = {
            'game': game,
        }

        return render(request, 'products/game_detail.html', context)
