from django.urls import path

from value import views

app_name = 'value'
urlpatterns = [
    path('create/', views.ValueCreateView.as_view(), name='create'),
    path('list/asset/<int:asset>/', views.ValueListView.as_view(), name='list'),
    path('update/<int:pk>/', views.ValueUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ValueDeleteView.as_view(), name='delete'),
]
