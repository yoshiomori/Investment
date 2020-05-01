import datetime

from django.contrib.auth import mixins as auth_mixins
from django.views import generic

import mixins
from asset.models import Asset
from value import forms, models


class ValueCreateView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.CreateView):
    model = models.Value
    fields = ['date', 'price', 'transaction']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.asset_id = self.kwargs['asset_id']
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        if 'asset_id' in self.kwargs:
            asset_name = Asset.objects.values_list('name', flat=True).get(pk=self.kwargs['asset_id'])
            kwargs['asset_name'] = asset_name
        return super().get_context_data(*args, **kwargs)

    def get_initial(self):
        date = datetime.date.today()
        return {'date': datetime.date(date.year, date.month, 1)}


class ValueListView(
    auth_mixins.LoginRequiredMixin,
    mixins.FilterAndOrderingListMixin,
    mixins.SetSessionPreviousUrlMixin,
    generic.ListView
):
    model = models.Value
    paginate_by = 100
    ordering = 'pk'
    filter_form_class = forms.ValueFilterForm
    ordering_form_class = forms.ValueOrderingForm

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(**self.kwargs)
        return queryset

    def get_context_data(self, *args, **kwargs):
        if 'asset_id' in self.kwargs:
            asset_name = Asset.objects.values_list('name', flat=True).get(pk=self.kwargs['asset_id'])
            kwargs['asset_name'] = asset_name
        return super().get_context_data(*args, **kwargs)


class ValueUpdateView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.UpdateView):
    model = models.Value
    fields = ['date', 'price', 'transaction']


class ValueDeleteView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.DeleteView):
    model = models.Value
