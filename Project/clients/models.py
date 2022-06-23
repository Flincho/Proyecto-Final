from django.db import models


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



