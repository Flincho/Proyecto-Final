from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from products.models import *


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('products:product-list')
    fields = ['name', 'category', 'price', 'stock', 'supplier', 'image', 'description']


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('products:product-list')
    fields = ['name', 'category', 'price', 'stock', 'supplier', 'image', 'description']


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:product-list')
