"""
Class views for the Home
"""
from django.views import View
from django.shortcuts import render


class Index(View):
    """
    Class view for the Home Index page
    """

    def get(self, request, *args, **kwargs):
        """
        GET method for the Home Index page
        """
        return render(request, 'home/index.html')
