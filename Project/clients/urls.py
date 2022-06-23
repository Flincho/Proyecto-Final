from django.urls import path
from clients import views


app_name = 'clients'
urlpatterns = [
    path('', views.ClientListView.as_view(), name='client-list'),
    path('client/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('client/<int:pk>/detail', views.ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update', views.ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete', views.ClientDeleteView.as_view(), name='client-delete'),
]
