"""
Class views for the Games / Products
"""
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Game, Category


class AllGames(View):
    """
    Custom Class view for the All Games page
    """

    def get(self, request):
        """
        GET method for the All Games page
        Used Boutique Ado project for logic and updated it
        to work in this project
        """
        games = Game.objects.all()
        query = None
        categories = None
        sort = None
        direction = None
        nav = None

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            nav = 'all_games'
            if sortkey == 'name':
                sortkey = 'lower_name'
                games = games.annotate(lower_name=Lower('name'))

            if sortkey == 'category_name':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            games = games.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            nav = 'genre'
            games = games.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('games'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            games = games.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
            'games': games,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
            'nav': nav
        }

        return render(request, 'products/games.html', context)


class GameDetail(View):
    """
    Custom Class view for a Game's details
    """

    def get(self, request, game_id):
        """
        Custom GET method for Game's details page
        """
        game = get_object_or_404(Game, pk=game_id)

        context = {
            'game': game,
            'nav': 'all_games'
        }

        return render(request, 'products/game_detail.html', context)
