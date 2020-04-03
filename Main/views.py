from django.db.models import Min, Max
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            value_dict = user.value_set.aggregate(Min('date'), Max('date'))
            date__min = value_dict['date__min']
            date__max = value_dict['date__max']
            if date__min and date__max:
                max_year = date__max.year
                max_month = date__max.month
                window_month = max_month - 3
                min_year = max_year if window_month > 0 else (max_year - 1)
                min_month = window_month if window_month > 0 else (window_month + 12)
                asset_queryset = user.asset_set.filter(hide=False)
                row_list = [['Year/Month'] + list(asset_queryset.values_list('name', flat=True))]
                while min_year < max_year or min_year == max_year and min_month <= max_month:
                    row = [f'{min_year}/{min_month}']
                    for asset in asset_queryset:
                        value = asset.value_set.filter(date__year=min_year, date__month=min_month).first()
                        if value is None:
                            row.append('null')
                        else:
                            initial_price = (value.price - value.delta)
                            if initial_price:
                                row.append(value.delta / initial_price)
                            else:
                                row.append('null')
                    row_list.append(row)
                    if min_month < 12:
                        min_month += 1
                    else:
                        min_month = 1
                        min_year += 1
                kwargs.update(dict(row_list=row_list))
        return super().get_context_data(**kwargs)
