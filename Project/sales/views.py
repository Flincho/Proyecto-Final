from django.shortcuts import render, redirect
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from datetime import datetime

from sales.models import *
from sales.forms import *
from accounts.models import *
from products.models import *


class SaleListView(ListView):
    model = Sale
    template_name = "sales/sale_list.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"


class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('sales:sale-list')


@login_required
def sale_form(request):
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        if sale_form.is_valid():
            data = sale_form.cleaned_data

            sale = Sale(
                client=data['client'],
                product=data['product'],
                unit_price=data['unit_price'],
                quantity=data['quantity'],
                final_price=data['final_price'],
                date=datetime.now().strftime("%Y-%m-%d"),
                seller=request.user
            )
            sale_approval = product_sale(data['product'], data['quantity'])
            if sale_approval == True:
                messages.success(request, "Sale Added")
                sale.save()
                return redirect("sales:sale-list")

            sale_form = SaleForm(request.POST)
            context_dict = {
                'sale_form': sale_form
            }
            messages.success(request, f"Sale failed: The curren stock ({sale_approval}) is not enough")
            return render(
                request=request,
                context=context_dict,
                template_name='sales/sale_form.html'
                )

    sale_form = SaleForm(request.POST)
    context_dict = {
        'sale_form': sale_form
        }
    return render(
        request=request,
        context=context_dict,
        template_name='sales/sale_form.html'
        )


@login_required
def sale_update(request, pk: int):
    sale = Sale.objects.get(pk=pk)
    prev_q = sale.quantity

    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        if sale_form.is_valid():
            data = sale_form.cleaned_data
            sale.client = data['client']
            sale.product = data['product']
            sale.unit_price = data['unit_price']
            sale.quantity = data['quantity']
            sale.final_price = data['final_price']

            sale_approval = product_sale(data['product'], data['quantity']-prev_q)
            if sale_approval == True:
                messages.success(request, "Sale Updated")
                sale.save()
                return redirect("sales:sale-list")

            sale_form = SaleForm(model_to_dict(sale))
            context_dict = {
                'sale': sale,
                'sale_form': sale_form,
            }
            messages.success(request, f"Sale failed: The curren stock ({sale_approval} un.) is not enough")

            return render(
                request=request,
                context=context_dict,
                template_name='sales/sale_form.html'
            )

    sale_form = SaleForm(model_to_dict(sale))
    context_dict = {
        'sale': sale,
        'sale_form': sale_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='sales/sale_form.html'
    )
