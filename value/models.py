from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Value(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    asset = models.ForeignKey('asset.Asset', on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
