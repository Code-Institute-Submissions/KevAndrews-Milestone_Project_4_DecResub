"""
Create a form for users to add wishlists
"""
from django import forms
from .models import Wishlist


class WishlistForm(forms.ModelForm):
    """
    Create a form for users to add Wishlists
    """
    class Meta:
        """
        Meta class for Wishlists
        """
        model = Wishlist
        exclude = (
            'user',
            'date_created',
            )

        fields = ['game_ids']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the Wishlist form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'game_ids': 'Game_ids',
        }

        # Add placeholders and classes to input fields
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].required = True
            self.fields[field].label = False
