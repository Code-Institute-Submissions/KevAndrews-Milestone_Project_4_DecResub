"""
URLs for the Profile pages
"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from profiles.views import Profile, OrderHistory

urlpatterns = [
    path('', login_required(Profile.as_view()), name='profile'),
    path('order_history/<order_number>',
         login_required(OrderHistory.as_view()), name='order_history'),
]
