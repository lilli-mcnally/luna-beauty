from django.db import models
from products.models import Product
from profiles.models import UserProfile

class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        unique_together = ('user_profile', 'product')
