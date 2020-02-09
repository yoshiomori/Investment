from accounts import models


def menu_bar(request):
    menu_bar_queryset = models.MenuBar.objects.all()
    return {
        'menu_bar': menu_bar_queryset
    }
