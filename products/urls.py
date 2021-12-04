"""
URLs for Games / Products App
"""
from django.urls import path
from products.views import AllGames, GameDetail

urlpatterns = [
    path('', AllGames.as_view(), name='games'),
    path('<game_id>', GameDetail.as_view(), name='game_detail'),
]
