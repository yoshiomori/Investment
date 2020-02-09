from django.contrib import admin

from asset.models import Asset

admin.site.register(Asset)


class ValueModelAdmin(admin.ModelAdmin):
    list_display = ('value', 'date')
    list_filter = ('asset', 'date')
