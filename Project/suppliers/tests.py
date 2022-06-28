from django.test import TestCase
from suppliers.models import Supplier
import random
import string


class TestModel(TestCase):
    def test_should_update_supplier(self):

        supplier = Supplier(
            name='supplier', email='email"email.com', phone=46546465, bank_account='Cadfgag6559')
        supplier.save()

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

            print(f'----------> Supplier Test values: {mock_name} -- {mock_email} -- {mock_num}')

            supplier.name =mock_name
            supplier.phone =mock_num
            supplier.email =mock_email
            supplier.bank_account =mock_name

            self.assertEqual(supplier.name, mock_name)
            self.assertEqual(supplier.phone, mock_num)
            self.assertEqual(supplier.email, mock_email)
            self.assertEqual(supplier.bank_account, mock_name)