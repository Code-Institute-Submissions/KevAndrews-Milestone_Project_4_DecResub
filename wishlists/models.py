"""
Custom Class
Wishlist models
"""
from django.db import models

from profiles.models import UserProfile
from products.models import Game


class Wishlist(models.Model):
    """
    Custom Class
    Creates a Wishlist model
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='Wishlist 1')
    games_list = models.ManyToManyField(Game, related_name="games")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
