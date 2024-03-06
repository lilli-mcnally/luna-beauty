from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
# Create your views here.

def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    product = Product.objects.get(pk=item_id)

    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    shade = None
    if 'shade' in request.POST:
        shade = request.POST['shade']

    bag = request.session.get('bag', {})

    if shade:
        if item_id in list(bag.keys()):
            if shade in bag[item_id]['items_by_shade'].keys():
                bag[item_id]['items_by_shade'][shade] += quantity
            else:
                bag[item_id]['items_by_shade'][shade] = quantity
        else:
            bag[item_id] = {'items_by_shade': {shade: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else: 
            bag[item_id] = quantity
            print('test')
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    quantity = int(request.POST.get('bag-quantity'))
    shade = None
    if 'shade' in request.POST:
        shade = request.POST['shade']
    bag = request.session.get('bag', {})
    if shade:
        if quantity > 0:
            bag[item_id]['items_by_shade'][shade] = quantity
        else:
            del bag[item_id]['items_by_shade'][shade]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    try:
        shade = None
        if 'shade' in request.POST:
            shade = request.POST['shade']
        bag = request.session.get('bag', {})

        if shade:
            del bag[item_id]['items_by_shade'][shade]
            if not bag[item_id]['items_by_shade']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)