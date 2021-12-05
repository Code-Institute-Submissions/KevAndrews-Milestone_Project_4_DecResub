"""
Calc Subtotal
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calc Subtotal
    """
    return price * quantity
