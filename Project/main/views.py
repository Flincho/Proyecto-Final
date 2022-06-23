from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from sales.models import *
from accounts.models import *
from clients.models import *
from suppliers.models import *
from products.models import *


def home(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}

    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="main/home.html")


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}

    # context_dict = dict()
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
        template_name="main/home.html",
    )

######################################################################

######################################################################

######################################################################

######################################################################
