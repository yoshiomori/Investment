from django import http
from django import urls
from django.contrib.auth import mixins as auth_mixins
from django.views import generic

import mixins
from asset import models


class AssetListView(auth_mixins.LoginRequiredMixin, mixins.SetSessionPreviousUrlMixin, generic.ListView):
    model = models.Asset
    paginate_by = 100
    ordering = 'pk'


class AssetCreateView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.CreateView):
    model = models.Asset
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AssetUpdateView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.Asset
    fields = ['name']

    def get_success_url(self):
        assert isinstance(self.request, http.HttpRequest)
        self.success_url = self.request.build_absolute_uri()
        return super().get_success_url()


class AssetDeleteView(auth_mixins.LoginRequiredMixin, mixins.SuccessUrlPreviousUrlMixin, generic.DeleteView):
    model = models.Asset
