"""
Code is from Boutique Ado example -
Models Class => contains models for Categories and Products
"""
from django.db import models


class Category(models.Model):
    """
    Code is from Boutique Ado example
    """

    class Meta:
        """
        Set Category to Categories in the Admin
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """
        Returns the Friendly name for the Category
        """
        return self.friendly_name


class Game(models.Model):
    """
    Code is from Boutique Ado example
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=False, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=False, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
