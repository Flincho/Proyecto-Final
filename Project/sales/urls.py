from django.urls import path

from sales import views

app_name = 'sales'
urlpatterns = [
    path('', views.SaleListView.as_view(), name='sale-list'),
    path('sale/add/', views.sale_form, name='sale-add'),
    path('sale/<int:pk>/detail', views.SaleDetailView.as_view(), name='sale-detail'),
    path('sale/<int:pk>/update', views.sale_update, name='sale-update'),
    path('sale/<int:pk>/delete', views.SaleDeleteView.as_view(), name='sale-delete'),
]
