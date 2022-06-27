from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from clients.models import *


class ClientListView(ListView):
    model = Client
    template_name = "clients/client_list.html"


class ClientDetailView(DetailView):
    model = Client
    template_name = "clients/client_detail.html"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    success_url = reverse_lazy('clients:client-list')
    fields = ['name', 'last_name', 'email', 'phone', 'rut', 'address']


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('clients:client-list')
    fields = ['name', 'last_name', 'email', 'phone', 'rut', 'address']


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client-list')

