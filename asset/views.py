from django.views import generic

import constants
import mixins
from asset import models
from django import http
from django.contrib.auth import mixins as auth_mixins
from django import urls


class AssetListView(auth_mixins.LoginRequiredMixin, mixins.PreviousUrlMixin, generic.ListView):
    model = models.Asset
    paginate_by = 100
    ordering = 'pk'


class AssetCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Asset
    fields = ['name']

    def get_success_url(self):
        self.success_url = self.request.build_absolute_uri(urls.reverse('asset:update', args=[self.object.pk]))
        return super().get_success_url()

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


class AssetDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = models.Asset

    def get_success_url(self):
        self.success_url = self.request.session[constants.PREVIOUS_URL]
        return super().get_success_url()
