from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator


class Supplier(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField(max_length=20)
    email = models.EmailField()
    bank_account = models.CharField(max_length=40)
    working_since = datetime.now().strftime("%d/%m/%Y")


class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField()
    price = models.IntegerField()
    stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField(max_length=20)
    rut = models.IntegerField(max_length=12, validators=[MinLengthValidator(12)])
    address = models.CharField(max_length=40)


#PRODUCT_CHOICES = list()
#for prod in Product.objects.all():
#    tuple = (prod.name, prod.name)
#    PRODUCT_CHOICES.append(tuple)

#CLIENT_CHOICES = list()
#for cli in Client.objects.all():
#    tuple = (cli.name, cli.name)
#    CLIENT_CHOICES.append(tuple)

class Sale(models.Model):
    #product = models.CharField(choices=PRODUCT_CHOICES)
    number = models.IntegerField()
    #final_price = number * product[1]
    #client = models.CharField(choices=CLIENT_CHOICES)
