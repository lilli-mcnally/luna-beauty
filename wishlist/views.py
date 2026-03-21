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

    item, created = Wishlist.objects.get_or_create(
        user_profile=user_profile,
        product=product,
    )

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(
        Wishlist,
        id=item_id,
        user_profile=request.user.userprofile
        )
    
    product_name = item.product.name

    item.delete()
    
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def move_to_bag(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id, user_profile=request.user.userprofile)
    product = item.product

    request.POST = request.POST.copy()
    request.POST['quantity'] = 1

    shade = request.POST.get('shade')
    if shade:
        request.POST['shade'] = shade
    
    response = add_to_bag(request, product.id)

    item.delete()
    return response