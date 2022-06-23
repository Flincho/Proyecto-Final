from django.urls import path
from suppliers import views


app_name = 'suppliers'
urlpatterns = [
    path('', views.SupplierListView.as_view(), name='supplier-list'),
    path('supplier/add/', views.SupplierCreateView.as_view(), name='supplier-add'),
    path('supplier/<int:pk>/detail', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/<int:pk>/update', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete', views.SupplierDeleteView.as_view(), name='supplier-delete'),
]
