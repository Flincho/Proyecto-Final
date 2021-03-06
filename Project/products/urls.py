from django.urls import path
from products import views


app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/detail', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name='product-delete'),

]
