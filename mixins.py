from django.forms import forms

FILTER = 'filter'

ORDERING = 'ordering'

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


class CleanNoneFormMixin(object):
    def clean(self):
        cleaned_data = super().clean()
        for key in [key for key, value in cleaned_data.items() if value is None]:
            del cleaned_data[key]
        return cleaned_data


class FilterAndOrderingListMixin(object):
    ordering_form_class = None
    filter_form_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.get_filter_form()
        if form.is_valid():
            queryset = queryset.filter(**form.cleaned_data)
        return queryset

    def get_filter_form(self):
        return self.get_filter_form_class()(data=self.request.GET)

    def get_filter_form_class(self):
        return self.filter_form_class

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, filter_form=self.get_filter_form(),
                                        ordering_form=self.get_ordering_form(), **kwargs)

    def get_ordering_form(self):
        return self.get_ordering_form_class()(data=self.request.GET)

    def get_ordering_form_class(self):
        assert issubclass(self.ordering_form_class, forms.Form)
        return self.ordering_form_class

    def get_ordering(self):
        form = self.get_ordering_form()
        if form.is_valid():
            self.ordering = form.cleaned_data[ORDERING]
        if self.ordering is None:
            self.ordering = 'pk'
        return super().get_ordering()
