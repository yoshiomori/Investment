import constants
from django import shortcuts


class PreviousUrlMixin(object):
    def dispatch(self, request, *args, **kwargs):
        request.session[constants.PREVIOUS_URL] = request.build_absolute_uri()
        return super().dispatch(request, *args, **kwargs)


class KwargsFilterQuerySetMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(**self.kwargs)


class KwargsUpdateSessionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        request.session.update(kwargs)
        return super().dispatch(request, *args, **kwargs)
