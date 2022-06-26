from django.db import models

from products.models import *
from clients.models import *


class Sale(models.Model):
    client = models.CharField(max_length=40, default=' ')
    product = models.CharField(max_length=40, default=' ')
    unit_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)
    date = models.DateField(default="2000-01-01")

