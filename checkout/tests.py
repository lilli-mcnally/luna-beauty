from django.test import TestCase
from .models import Order, OrderLineItem
from decimal import *

# Create your tests here.
class TestOrder(TestCase):

    def setUp(self):
        Order.objects.create(
            order_number = "0147258369",
            full_name = "New Test",
            email = "test@test.com",
            phone = "0369258147",
            street_address1 = "1 Address Street",
            town_or_city = "Some Town",
            country = "United Kingdom",
            delivery_cost = "3.50",
            discount = "5",
            order_total = "50",
            grand_total = "53.50",
            original_bag = "MAC Matte Lipstick",
            stripe_pid = "teststripepid",
            )
    
    def test_order_number(self):
        """ Testing whether the order number is correct """
        test_order = Order.objects.get(stripe_pid="teststripepid")
        self.assertEqual(test_order.order_number, "0147258369")

    def test_full_name(self):
        """ Testing whether the name is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.full_name, "New Test")

    def test_email(self):
        """ Testing whether the email is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.email, "test@test.com")
    
    def test_phone(self):
        """ Testing whether the phone is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.phone, "0369258147")

    def test_street_address1(self):
        """ Testing whether the street address is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.street_address1, "1 Address Street")

    def test_town_or_city(self):
        """ Testing whether the town or city is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.town_or_city, "Some Town")

    def test_country(self):
        """ Testing whether the country is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.country, "United Kingdom")

    def test_delivery_cost(self):
        """ Testing whether the delivery cost is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.delivery_cost, Decimal("3.50"))
    
    def test_order_total(self):
        """ Testing whether the order total is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.order_total, Decimal("50"))

    def test_grand_total(self):
        """ Testing whether the grand total is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.grand_total, Decimal("53.50"))

    def test_original_bag(self):
        """ Testing whether the original bag is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.original_bag, "MAC Matte Lipstick")

    def test_stripe_pid(self):
        """ Testing whether the stripe pid is correct """
        test_order = Order.objects.get(order_number = "0147258369")
        self.assertEqual(test_order.stripe_pid, "teststripepid")