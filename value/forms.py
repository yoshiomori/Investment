from django.forms import forms, models, fields

import mixins
from value import models as value_models


class SessionVersionValueForm(models.ModelForm):
    class Meta:
        model = value_models.Value
        fields = ['asset']


class ValueFilterForm(mixins.CleanNoneFormMixin, forms.Form):
    date__gte = fields.DateField(required=False, label='Initial Date')
    date__lte = fields.DateField(required=False, label='Final Date')

    class Media:
        js = ('js/value_list.js',)


class ValueOrderingForm(mixins.CleanNoneFormMixin, forms.Form):
    ordering = fields\
        .ChoiceField(choices=[('date', 'Ascending Date'), ('-date', 'Descending Date'), ('price', 'Ascending Price'),
                              ('-price', 'Descending Price'), ('asset_id', 'Ascending Asset Id'),
                              ('-asset_id', 'Descending Asset Id')],
                     required=False)
