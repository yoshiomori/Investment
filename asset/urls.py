from django.urls import path, include

from asset import views

app_name = 'asset'
urlpatterns = [
    path('', views.AssetListView.as_view(), name='list'),
    path('create/', views.AssetCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.AssetUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AssetDeleteView.as_view(), name='delete'),
    path('<int:asset_id>/value/', include('value.urls')),
]
