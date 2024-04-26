from django.test import TestCase
from .models import Product, Category
from decimal import *

# Create your tests here.

class TestCategory(TestCase):

    def setUp(self):
        Category.objects.create(
        name = "makeup_brushes",
        friendly_name =  "Makeup Brushes",
        )

    def test_name(self):
        """ Testing whether the name is correct """
        test_category = Category.objects.get(friendly_name =  "Makeup Brushes")
        self.assertEqual(test_category.name,"makeup_brushes")
    
    def test_friendly_name(self):
        """ Testing whether the friendly_name is correct """
        test_category = Category.objects.get(name = "makeup_brushes")
        self.assertEqual(test_category.friendly_name,  "Makeup Brushes")


class TestProduct(TestCase):

    def setUp(self):
        Product.objects.create(
        sku = "0123456789",
        name = "NXY Foundation Brush",
        description = "Test description about the NXY Foundation Brush",
        price = "10.00",
        rating = "4",
        )
    
    def test_sku(self):
        """ Testing whether the sku is correct """
        test_product = Product.objects.get(name = "NXY Foundation Brush")
        self.assertEqual(test_product.sku, "0123456789")
    
    def test_name(self):
        """ Testing whether the name is correct """
        test_product = Product.objects.get(sku = "0123456789")
        self.assertEqual(test_product.name, "NXY Foundation Brush")
    
    def test_description(self):
        """ Testing whether the description is correct """
        test_product = Product.objects.get(sku = "0123456789")
        self.assertEqual(test_product.description, "Test description about the NXY Foundation Brush")
    
    def test_price(self):
        """ Testing whether the price is correct """
        test_product = Product.objects.get(sku = "0123456789")
        self.assertEqual(test_product.price, Decimal("10.00"))
    
    def test_rating(self):
        """ Testing whether the rating is correct """
        test_product = Product.objects.get(sku = "0123456789")
        self.assertEqual(test_product.rating, Decimal("4"))
    