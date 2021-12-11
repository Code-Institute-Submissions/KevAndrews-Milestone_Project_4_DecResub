"""
URLs for Games / Products App
"""
from django.urls import path
from products.views import AllGames, GameDetail
from . import views

urlpatterns = [
    path('', AllGames.as_view(), name='games'),
    path('<int:game_id>/', GameDetail.as_view(), name='game_detail'),
    path('add/', views.add_game, name='add_game'),
]
