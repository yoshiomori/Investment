from django import template

register = template.Library()


@register.filter
def percent(value):
    return f'{value:,.2%}'
