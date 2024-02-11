from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):

    class Meta:
        # Tells Django Admin to put Categories not Categorys 
        verbose_name_plural = "Categories" 

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    volume = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(null=True, blank=True)
    shades = ArrayField(models.CharField(max_length=200, null=True, blank=True))

    def __str__(self):
        return self.name