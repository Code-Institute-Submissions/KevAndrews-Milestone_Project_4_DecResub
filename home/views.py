"""
Class views for the Home
"""
from django.http import HttpResponse
from django.views import View


class Index(View):
    """
    Class view for the Home Index page
    """

    def get(self, request):
        """
        GET method for the Home Index page
        """
        return HttpResponse(request)
