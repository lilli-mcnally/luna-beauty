from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'product', 'shade')
    list_filter = ('user_profile', 'product')
    search_fields = ('user_profile__user__username', 'product__name', 'shade')

