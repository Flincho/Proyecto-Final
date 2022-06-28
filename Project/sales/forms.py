from django import forms
import calculation
from products.models import *
from clients.models import *


class SaleForm(forms.Form):
    client = forms.ChoiceField(choices=client_choices(), label='Client', required=False)
    product = forms.ChoiceField(choices=product_choices(), label='Product', required=False)
    unit_price = forms.IntegerField(label='Unit Price', required=False)
    quantity = forms.IntegerField(label='Quantity', required=False)
    final_price = forms.IntegerField(
        label='Final Price',
        widget=calculation.FormulaInput('quantity*unit_price'),
        required=False
    )

