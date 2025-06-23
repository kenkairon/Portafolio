# tu_app/templatetags/text_filters.py
from django import template

register = template.Library()

@register.filter
def splitlines(value):
    if value:
        return value.splitlines()
    return []
