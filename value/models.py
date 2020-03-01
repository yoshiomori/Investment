from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Value(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    asset = models.ForeignKey('asset.Asset', on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    delta = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('date',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        last = self.asset.value_set.values_list('price', flat=True).last()
        if last is None:
            last = 0
        self.delta = self.price - last
        super().save(force_insert, force_update, using, update_fields)
