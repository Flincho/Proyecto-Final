from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.test import Client
from accounts.models import *
from accounts.views import *


class TestModel(TestCase):
    def test_should_login(self):

        c = Client()
        response = c.post('/accounts/login/', {'username': 'admin', 'password': 'admin'})

        form = AuthenticationForm(response, data=response)

        username = 'admin'
        password = 'admin'
        user = authenticate(username=username, password=password)



        print(user)

        self.assertEqual(user, 'admin')
