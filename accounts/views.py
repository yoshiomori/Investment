from django.views import generic
from django.contrib.auth import mixins


class ProfileTemplateView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'
