from django.db import models
from products.models import Product
from profiles.models import UserProfile

class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    chosen_shade = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.chosen_shade:
            return f"{self.product.name} - {self.chosen_shade}"
        return self.product.name

    class Meta:
        unique_together = ('user_profile', 'product', 'chosen_shade')
