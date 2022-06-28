from django.test import TestCase
from clients.models import Client
import random
import string


class TestModel(TestCase):
    def test_should_create_client(self):
        for _ in range(10):
            KEY_LEN = 12
            char_list = [
                random.choice((string.ascii_letters + string.digits))
                for _ in range(KEY_LEN)
            ]
            mock_name = ''.join(char_list)

            mock_email = f'{mock_name}@{mock_name}.com'

            num_list = [
                random.choice((string.digits))
                for _ in range(KEY_LEN)
            ]
            mock_num = ''.join(num_list)
            mock_num = int(mock_num)

            print(f'----------> Test values: {mock_name} -- {mock_email} -- {mock_num}')

            client = Client(
                name=mock_name, last_name=mock_name, email=mock_email, phone=mock_num, rut=mock_num, address=mock_name )

            client.save()

            self.assertEqual(client.name, mock_name)
            self.assertEqual(client.email, mock_email)
            self.assertEqual(client.phone, mock_num)