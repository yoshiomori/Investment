PREVIOUS_URL = 'previous list url'


class SetSessionPreviousUrlMixin(object):
    def dispatch(self, request, *args, **kwargs):
        request.session[PREVIOUS_URL] = request.build_absolute_uri()
        return super().dispatch(request, *args, **kwargs)


class KwargsFilterQuerySetMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(**self.kwargs)


class KwargsUpdateSessionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        request.session.update(kwargs)
        return super().dispatch(request, *args, **kwargs)


class SuccessUrlPreviousUrlMixin(object):
    def get_success_url(self):
        self.success_url = self.request.session[PREVIOUS_URL]
        return super().get_success_url()
