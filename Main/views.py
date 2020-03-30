from django.db.models import Min, Max
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            value_dict = user.value_set.aggregate(Min('date'), Max('date'))
            date = value_dict['date__min']
            date__max = value_dict['date__max']
            if date and date__max:
                year = date.year
                month = date.month
                max_year = date__max.year
                max_month = date__max.month
                asset_queryset = user.asset_set.all()
                row_list = [['Year/Month'] + list(asset_queryset.values_list('name', flat=True))]
                while (month <= max_month or year < max_year) and (year != max_year or month <= max_month):
                    row = [f'{year}/{month}']
                    for asset in asset_queryset:
                        value = asset.value_set.filter(date__year=year, date__month=month).first()
                        if value is None:
                            row.append(0)
                        else:
                            initial_price = (value.price - value.delta)
                            if initial_price:
                                row.append(value.delta / initial_price)
                            else:
                                row.append(0)
                    row_list.append(row)
                    if month < 12:
                        month += 1
                    else:
                        month = 1
                        year += 1
                kwargs.update(dict(row_list=row_list))
        return super().get_context_data(**kwargs)
