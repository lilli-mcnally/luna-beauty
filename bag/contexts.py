from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    discounted_total = 0
    total_from_discount = 0
    bag = request.session.get('bag', {})
    delivery = Decimal(settings.DELIVERY)

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
        discounted_total = total - discount
        grand_total = discounted_total + delivery
    else:
        discounted_total = total
        grand_total = total + delivery

    total_from_discount = Decimal(settings.DISCOUNT_THRESHOLD - total)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'discount': discount,
        'discounted_total': discounted_total,
        'grand_total': grand_total,
        'delivery': delivery,
        'total_from_discount': total_from_discount,
    }

    return context
