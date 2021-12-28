"""
Admin Class for Review
"""
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin Class for Review
    """
    list_display = (
        'title',
        'game',
        'user',
        'date_created'
    )
