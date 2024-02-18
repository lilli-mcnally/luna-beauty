from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    discount_total = 0

    if total >= settings.DISCOUNT_THRESHOLD:
        discount = Decimal((total / 100) * DISCOUNT_PERCENTAGE)
        grand_total = total - discount
    else:
        grand_total = total
    

    context = {
    'bag_items': bag_items,
    'total': total,
    'product_count': product_count,
    'discount_threshold': settings.DISCOUNT_THRESHOLD,
    'discount_percentage': settings.DISCOUNT_PERCENTAGE,
    'discount': discount,
    'grand_total': discount_total,
    'delivery': settings.DELIVERY,
    }

    return context