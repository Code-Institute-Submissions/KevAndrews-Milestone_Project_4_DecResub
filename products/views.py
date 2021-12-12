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
from .forms import GameForm


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
        nav = 'all_games'

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


@login_required
def add_game(request):
    """ Add a game to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            messages.success(request, 'Successfully added game!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(
                request,
                'Failed to add game. Please ensure the form is valid.'
            )
    else:
        form = GameForm()

    template = 'products/add_game.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_game(request, game_id):
    """ Edit a game in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated game!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(
                request,
                'Failed to update game. Please ensure the form is valid.'
            )
    else:
        form = GameForm(instance=game)
        messages.info(request, f'You are editing {game.name}')

    template = 'products/edit_game.html'
    context = {
        'form': form,
        'game': game,
    }

    return render(request, template, context)


@login_required
def delete_game(request, game_id):
    """ Delete a game from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'Game deleted!')
    return redirect(reverse('games'))
    """ Delete a Game in the store """
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'Game deleted!')

    return redirect(reverse('games'))
