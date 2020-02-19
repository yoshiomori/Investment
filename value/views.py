from django.contrib.auth import mixins as auth_mixins
from django.views import generic

import mixins
from value import forms, models


class ValueCreateView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.CreateView):
    model = models.Value
    fields = ['date', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.asset_id = self.kwargs['asset_id']
        return super().form_valid(form)


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


class ValueUpdateView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.UpdateView):
    model = models.Value
    fields = ['date', 'price']


class ValueDeleteView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.DeleteView):
    model = models.Value
