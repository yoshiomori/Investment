from django import template
from django.db.models import Sum

register = template.Library()


@register.filter
def sum_delta(asset_list):
    return asset_list.values('name').annotate(sum=Sum('value__delta'))
