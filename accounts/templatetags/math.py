from django import template

register = template.Library()


@register.filter
def percent(value):
    if isinstance(value, str):
        return value
    return f'{value:,.2%}'
