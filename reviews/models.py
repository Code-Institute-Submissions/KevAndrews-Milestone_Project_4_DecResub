"""
Custom Class
Review models
"""
from django.db import models

from profiles.models import UserProfile
from products.models import Game


class Review(models.Model):
    """
    Custom Class
    Creates a review model
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
