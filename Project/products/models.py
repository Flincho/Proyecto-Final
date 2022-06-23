from django.db import models
#from main.models import supplier_choices


#def supplier_choices():
#    SUPPLIER_CHOICES = list()
#    for sup in Supplier.objects.all():
#        tuple = (sup.name, sup.name)
#        SUPPLIER_CHOICES.append(tuple)
#    return SUPPLIER_CHOICES

class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    price = models.IntegerField()
    stock = models.IntegerField()
    #choices=supplier_choices()
    supplier = models.CharField(max_length=40, default='')
    image = models.ImageField(upload_to='prod_img', null=True, blank=True)




