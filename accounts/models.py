from django.db import models
from django.urls import reverse


class MenuBar(models.Model):
    view_name = models.CharField(max_length=255)
    http_inner = models.CharField(max_length=255)
    order = models.IntegerField(null=True, blank=True)
    group = models.CharField(max_length=255, null=True, blank=True)
    show_only_when = models.IntegerField(
        choices=((0, 'Not Authenticated'), (1, 'Authenticated')),
        null=True,
        blank=True
    )

    @property
    def href(self):
        return reverse(self.view_name)

    class Meta:
        ordering = ['order']
