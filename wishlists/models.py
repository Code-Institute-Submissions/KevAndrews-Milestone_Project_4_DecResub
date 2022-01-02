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
    game_ids = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
