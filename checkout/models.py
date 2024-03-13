import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=20, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town_or_city = models.CharField(max_length=60, null=False, blank=False)
    county = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    shade = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegrerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, editable=False)