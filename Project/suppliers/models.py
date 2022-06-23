from django.db import models
#from main.models import supplier_choices


def supplier_choices():
    SUPPLIER_CHOICES = list()
    for sup in Supplier.objects.all():
        tuple = (sup.name, sup.name)
        SUPPLIER_CHOICES.append(tuple)
    return SUPPLIER_CHOICES


class Supplier(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.EmailField()
    bank_account = models.CharField(max_length=40)
    working_since = models.DateField(default="2000-01-01")






