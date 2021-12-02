"""
Code is from Boutique Ado example -
Handles the Product and Category Admin
"""
from django.contrib import admin
from .models import Game, Category


class GameAdmin(admin.ModelAdmin):
    """
    Code is from Boutique Ado example
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Code is from Boutique Ado example
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)
