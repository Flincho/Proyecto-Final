from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from suppliers.models import *


class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier/supplier_list.html"


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "supplier/supplier_detail.html"


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    success_url = reverse_lazy('suppliers:supplier-list')
    fields = ['name', 'phone', 'email', 'bank_account', 'working_since']


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    success_url = reverse_lazy('suppliers:supplier-list')
    fields = ['name', 'phone', 'email', 'bank_account']


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers:supplier-list')
