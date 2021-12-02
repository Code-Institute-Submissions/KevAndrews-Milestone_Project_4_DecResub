"""
URLs for Games / Products App
"""
from django.urls import path
from products.views import AllGames

urlpatterns = [
    path('', AllGames.as_view(), name='games'),
]
