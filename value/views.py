from django.contrib.auth import mixins as auth_mixins
from django.views import generic

import constants
import mixins
from value import models
from value import forms
from django import urls

from asset import models as asset_models


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
    mixins.PreviousUrlMixin,
    mixins.KwargsFilterQuerySetMixin,
    mixins.KwargsUpdateSessionMixin,
    generic.ListView
):
    model = models.Value
    paginate_by = 100
    ordering = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        asset = asset_models.Asset.objects.values_list('name', flat=True).filter(pk=self.kwargs.get('asset')).first()
        return super().get_context_data(object_list=object_list, asset=asset, **kwargs)


class ValueUpdateView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Value
    fields = ['date', 'price']


class ValueDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Value

    def get_success_url(self):
        self.success_url = self.request.session[constants.PREVIOUS_URL]
        return super().get_success_url()
