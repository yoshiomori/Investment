from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
