from django.forms import forms, models
from value import models as value_models


class SessionVersionValueForm(models.ModelForm):
    class Meta:
        model = value_models.Value
        fields = ['asset']
