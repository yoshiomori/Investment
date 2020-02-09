from django.db import models
from django.urls import reverse


class MenuBar(models.Model):
    view_name = models.CharField(max_length=255)
    http_inner = models.CharField(max_length=255)

    @property
    def href(self):
        return reverse(self.view_name)
