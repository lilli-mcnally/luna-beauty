from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    total_from_discount = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for shade, quantity in item_data['items_by_shade'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'shade': shade,
                })

    if total >= settings.DISCOUNT_THRESHOLD:
        discount = Decimal((total / 100) * settings.DISCOUNT_PERCENTAGE)
        grand_total = total - discount
    else:
        grand_total = total

    total_from_discount = Decimal(settings.DISCOUNT_THRESHOLD - grand_total)
    

    context = {
    'bag_items': bag_items,
    'total': total,
    'product_count': product_count,
    'discount_threshold': settings.DISCOUNT_THRESHOLD,
    'discount_percentage': settings.DISCOUNT_PERCENTAGE,
    'discount': discount,
    'grand_total': grand_total,
    'delivery': settings.DELIVERY,
    'total_from_discount': total_from_discount,
    }

    return context