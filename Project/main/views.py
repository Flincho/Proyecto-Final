from django.shortcuts import render
from django.db.models import Q
from accounts.views import get_avatar_url_ctx

from sales.models import *
from accounts.models import *
from clients.models import *
from suppliers.models import *
from products.models import *


def home(request):
    try:
        avatar_ctx = get_avatar_url_ctx(request)
        context_dict = {**avatar_ctx}

        return render(
            request=request,
            context=context_dict,
            template_name="main/home.html")
    except:
        return render(
            request=request,
            template_name="main/home.html")


def search(request):
    try:
        avatar_ctx = get_avatar_url_ctx(request)
        context_dict = {**avatar_ctx}
    except:
        context_dict = {}

    if request.GET['client_search']:
        search_param = request.GET['client_search']
        query = Q(name__contains=search_param)
        query.add(Q(last_name__contains=search_param), Q.OR)
        clients = Client.objects.filter(query)
        context_dict.update({
            'clients': clients,
            'client_search': search_param,
            'product_search': None,
            'supplier_search': None,
        })
    elif request.GET['product_search']:
        search_param = request.GET['product_search']
        products = Product.objects.filter(name__contains=search_param)
        context_dict.update({
            'products': products,
            'product_search': search_param,
            'client_search': None,
            'supplier_search': None,
        })
    elif request.GET['supplier_search']:
        search_param = request.GET['supplier_search']
        suppliers = Supplier.objects.filter(name__contains=search_param)
        context_dict.update({
            'suppliers': suppliers,
            'supplier_search': search_param,
            'client_search': None,
            'product_search': None,
        })

    return render(
        request=request,
        context=context_dict,
        template_name="main/home.html",
    )


def about(request):
    try:
        avatar_ctx = get_avatar_url_ctx(request)
        context_dict = {**avatar_ctx}

        return render(
            request=request,
            context=context_dict,
            template_name="main/about.html")

    except:
        return render(
            request=request,
            template_name="main/about.html")
