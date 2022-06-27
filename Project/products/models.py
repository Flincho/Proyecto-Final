from django.db import models
from suppliers.models import *


class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    category = models.CharField(max_length=40)
    price = models.IntegerField()
    stock = models.IntegerField()
    supplier = models.CharField(max_length=40, choices=supplier_choices(), default='')
    image = models.ImageField(upload_to='prod_img/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)


def product_choices():
    PRODUCT_CHOICES = [(' ', ' ')]
    for prod in Product.objects.all():
        tuple = (prod.name, prod.name)
        PRODUCT_CHOICES.append(tuple)
    return PRODUCT_CHOICES


def product_sale(product, sale_q):
    product = Product.objects.get(name=product)
    stock = product.stock
    if sale_q <= stock:
        product.stock = stock-sale_q
        product.save()
        return True
    else:
        return stock




