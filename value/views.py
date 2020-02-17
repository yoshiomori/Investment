from django.contrib.auth import mixins as auth_mixins
from django.views import generic

import mixins
from value import models
from value import forms
from django import urls


class ValueCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Value
    fields = ['date', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        session_version_value_form = forms.SessionVersionValueForm(self.request.session, instance=form.instance)
        if session_version_value_form.is_valid():
            session_version_value_form.save(commit=False)
        else:
            raise RuntimeError('Formulário SessionVersionValueForm deve ser válido na sessão')
        return super().form_valid(form)

    def get_success_url(self):
        self.success_url = urls.reverse_lazy('value:list', args=[self.request.session['asset']])
        return super().get_success_url()


class ValueListView(
    auth_mixins.LoginRequiredMixin,
    mixins.FilterAndOrderingListMixin,
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
