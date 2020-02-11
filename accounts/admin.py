from django.contrib import admin
from accounts import models


class MenuBarModelAdmin(admin.ModelAdmin):
    list_display = ('http_inner', 'view_name', 'order', 'group')
    list_filter = ('view_name', 'http_inner')


admin.site.register(models.MenuBar, MenuBarModelAdmin)
