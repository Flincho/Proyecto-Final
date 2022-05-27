from django.contrib import admin

from app_1.models import *
admin.site.register(Supplier)

admin.site.register(Product)

admin.site.register(Client)

admin.site.register(Sale)
