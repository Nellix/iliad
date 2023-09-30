# In your tests.py file

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date
from .models import Order, OrderItem


class OrderSearchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Add test data to the database, create sample orders and items
        self.order1 = Order.objects.create(orderId= "PP040023123",shipping_price="1000.00")
        self.order2 = Order.objects.create(orderId= "PP040023121",shipping_price="1000.00")

        self.item1_order1 = OrderItem.objects.create(order=self.order1, barcode="123456", price=100, quantity=2, cost=100,tax_perc=10,tax_amt=1)
        self.item2_order1 = OrderItem.objects.create(order=self.order1, barcode="789012", price=50, quantity=1, cost=100,tax_perc=10,tax_amt=1)

        self.item1_order2 = OrderItem.objects.create(order=self.order2, barcode="456789", price=75, quantity=3, cost=134,tax_perc=10,tax_amt=1)

    def test_valid_orders_search(self):
        # Test a valid request
        data = {
            'count': 2,
            'date_from': '2023-09-01',
            'date_to': '2023-09-30',
        }

        response = self.client.post('/api/orders_search/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one order matches the criteria
        # Add more specific assertions based on your data model and the expected response

    def test_invalid_count_value(self):
        # Test when an invalid count value is provided
        data = {
            'count': 25,  # Invalid count value
            'date_from': '2023-09-01',
            'date_to': '2023-09-30',
        }

        response = self.client.post('/api/orders_search/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Add assertions for the expected error response

    def test_invalid_date_format(self):
        # Test when an invalid date format is provided
        data = {
            'count': 2,
            'date_from': '2023-09-01', 
            'date_to': '20230930', # Invalid date format
        }

        response = self.client.post('/api/orders_search/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Add assertions for the expected error response

