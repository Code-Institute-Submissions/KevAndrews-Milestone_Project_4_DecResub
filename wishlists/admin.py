"""
Admin Class for Wishlist
"""
from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """
    Admin Class for Wishlist
    """
    list_display = (
        'user',
        'date_created'
    )
