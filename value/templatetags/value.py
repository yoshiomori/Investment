from django import template
from django.db.models import Sum

register = template.Library()


@register.filter
def sum_group_by_date_value_filter(value_list):
    d = {}
    for date, delta, price in value_list.values_list('date', 'delta', 'price'):
        d.setdefault(date, {'date': date, 'delta': 0, 'price': 0})
        d[date]['delta'] += delta
        d[date]['price'] += price
    return d.values()
