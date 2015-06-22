__author__ = 'PerminovMA@live.ru'

from django.template import Library

register = Library()


@register.filter(name='get_field_type')
def get_field_type(field):
    """Return HTML input field type"""
    field_type = field.field.widget.__class__.__name__
    if field_type.endswith("Input"):
        field_type = field_type[:-5]
    return field_type