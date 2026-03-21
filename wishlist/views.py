from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bag.views import add_to_bag

from .models import Wishlist
from products.models import Product

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(
        user_profile=request.user.userprofile
    )

    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = request.user.userprofile

    shade = request.POST.get('shade')

    item, created = Wishlist.objects.get_or_create(
        user_profile=user_profile,
        product=product,
        shade=shade
    )

    if created:
        messages.success(request, f'{product.name} was added to your wishlist!')
    else:
        messages.info(request, f'{product.name} is already on your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(
        Wishlist,
        id=item_id,
        user_profile=request.user.userprofile
        )
    
    product_name = item.product.name
    shade = item.shade

    item.delete()

    if shade:
        messages.success(request, f'{product_name} - {shade} was removed from your wishlist')
    else:
        messages.success(request, f'{product_name} was removed from your wishlist')


@login_required
def move_to_bag(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id, user_profile=request.user.userprofile)
    product = item.product
    shade = item.shade

    request.POST = request.POST.copy()
    request.POST['quantity'] = 1
    if shade:
        request.POST['shade'] = shade
    
    response = add_to_bag(request, product.id)

    item.delete()
    return response