from django.db import models
from products.models import Product
from profiles.models import UserProfile

class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shade = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.shade:
            return f"{self.product.name} - {self.shade}"
        return self.product.name

    class Meta:
        unique_together = ('user_profile', 'product', 'shade')
