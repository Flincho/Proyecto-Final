from django.urls import path

from app_1 import views

app_name = 'app_1'
urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search, name='search'),

    path('suppliers', views.SupplierListView.as_view(), name='supplier-list'),
    path('supplier/add/', views.SupplierCreateView.as_view(), name='supplier-add'),
    path('supplier/<int:pk>/detail', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/<int:pk>/update', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete', views.SupplierDeleteView.as_view(), name='supplier-delete'),

    path('clients', views.ClientListView.as_view(), name='client-list'),
    path('client/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('client/<int:pk>/detail', views.ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update', views.ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete', views.ClientDeleteView.as_view(), name='client-delete'),

    path('products', views.ProductListView.as_view(), name='product-list'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/detail', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name='product-delete'),

    path('sales', views.SaleListView.as_view(), name='sale-list'),
    path('sale/add/', views.SaleCreateView.as_view(), name='sale-add'),
    path('sale/<int:pk>/detail', views.SaleDetailView.as_view(), name='sale-detail'),
    path('sale/<int:pk>/update', views.SaleUpdateView.as_view(), name='sale-update'),
    path('sale/<int:pk>/delete', views.SaleDeleteView.as_view(), name='sale-delete'),

]
