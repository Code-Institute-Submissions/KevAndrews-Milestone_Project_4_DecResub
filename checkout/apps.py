"""
Used Code from the Boutique Ado project
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Used Code from the Boutique Ado project
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
