from django import template
from django.db.models import Sum

register = template.Library()


@register.filter
def sum_group_by_date_value_filter(value_list):
    return value_list.values('date').annotate(delta=Sum('delta'), price=Sum('price'))
