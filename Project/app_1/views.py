from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from app_1.models import *
from accounts.models import *


def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}

    print('context_dict: ', context_dict, avatar_ctx)
    return render(
        request=request,
        context=context_dict,
        template_name="app_1/home.html")


#def get_avatar(request):
#    avatar = Ava


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}


    #context_dict = dict()
    if request.GET['client_search']:
        search_param = request.GET['client_search']
        query = Q(name__contains=search_param)
        query.add(Q(last_name__contains=search_param), Q.OR)
        clients = Client.objects.filter(name__contains=search_param)
        context_dict.update({
            'clients': clients
        })
    elif request.GET['product_search']:
        search_param = request.GET['product_search']
        products = Product.objects.filter(name__contains=search_param)
        context_dict.update({
            'products': products
        })
    elif request.GET['supplier_search']:
        search_param = request.GET['supplier_search']
        suppliers = Supplier.objects.filter(name__contains=search_param)
        context_dict.update({
            'suppliers': suppliers
        })

    return render(
        request=request,
        context=context_dict,
        template_name="app_1/home.html",
    )

###############################################################

class SupplierListView(ListView):
    model = Supplier
    template_name = "app_1/supplier_list.html"


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "app_1/supplier_detail.html"


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    success_url = reverse_lazy('app_1:supplier-list')
    fields = ['name', 'phone', 'email', 'bank_account', 'working_since']


class SupplierUpdateView(LoginRequiredMixin,UpdateView):
    model = Supplier
    success_url = reverse_lazy('app_1:supplier-list')
    fields = ['name', 'phone', 'email', 'bank_account']


class SupplierDeleteView(LoginRequiredMixin,DeleteView):
    model = Supplier
    success_url = reverse_lazy('app_1:supplier-list')

###############################################################


class ClientListView(ListView):
    model = Client
    template_name = "app_1/client_list.html"


class ClientDetailView(DetailView):
    model = Client
    template_name = "app_1/client_detail.html"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    success_url = reverse_lazy('app_1:client-list')
    fields = ['name', 'last_name', 'email', 'phone', 'rut', 'address']


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('app_1:client-list')
    fields = ['name', 'last_name', 'email', 'phone', 'rut', 'address']


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('app_1:client-list')

##########################################################################


class ProductListView(ListView):
    model = Product
    template_name = "app_1/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "app_1/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('app_1:product-list')
    fields = ['name', 'category', 'price', 'stock', 'supplier']


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('app_1:product-list')
    fields = ['name', 'category', 'price', 'stock', 'supplier']


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('app_1:product-list')
    

########################################################################


class SaleListView(ListView):
    model = Sale
    template_name = "app_1/sale_list.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "app_1/sale_detail.html"


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    success_url = reverse_lazy('app_1:sale-list')
    fields = ['product', 'quantity', 'client']


class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model = Sale
    success_url = reverse_lazy('app_1:sale-list')
    fields = ['product', 'quantity', 'client']


class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('app_1:sale-list')
