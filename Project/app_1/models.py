from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.EmailField()
    bank_account = models.CharField(max_length=40)
    working_since = models.DateField(default="2000-01-01")


def supplier_choices():
    SUPPLIER_CHOICES = list()
    for sup in Supplier.objects.all():
        tuple = (sup.name, sup.name)
        SUPPLIER_CHOICES.append(tuple)
    return SUPPLIER_CHOICES


class Client(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    rut = models.IntegerField()
    address = models.CharField(max_length=40)


def client_choices():
    CLIENT_CHOICES = list()
    for cli in Client.objects.all():
        tuple = (f'{cli.name} {cli.last_name}', f'{cli.name} {cli.last_name}')
        CLIENT_CHOICES.append(tuple)
    return CLIENT_CHOICES


class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    price = models.IntegerField()
    stock = models.IntegerField()
    supplier = models.CharField(max_length=40, choices=supplier_choices())
    #image = models.ImageField(upload_to='avatars', null=True, blank=True)


def product_choices():
    PRODUCT_CHOICES = list()
    for prod in Product.objects.all():
        tuple = (prod.name, prod.name)
        PRODUCT_CHOICES.append(tuple)
    return PRODUCT_CHOICES


class Sale(models.Model):
    product = models.CharField(max_length=40, choices=product_choices(), default='.')
    quantity = models.IntegerField()
    #final_price = number * product[1]
    client = models.CharField(max_length=40, choices=client_choices(), default='.')
