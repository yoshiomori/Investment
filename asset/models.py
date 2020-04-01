from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.name
