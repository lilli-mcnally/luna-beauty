from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
# Create your views here.

def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    shade = None
    if 'shade' in request.POST:
        shade = request.POST['shade']

    bag = request.session.get('bag', {})
    print(request.POST)

    if shade:
        print(shade)
        if item_id in list(bag.keys()):
            if shade in bag[item_id]['items_by_shade'].keys():
                bag[item_id]['items_by_shade'][shade] += quantity
                messages.success(request, f'{product.name} - {shade}  was added to your bag')
            else:
                bag[item_id]['items_by_shade'][shade] = quantity
                messages.success(request, f'{product.name} - {shade}  was added to your bag')
        else:
            bag[item_id] = {'items_by_shade': {shade: quantity}}
            messages.success(request, f'{product.name} - {shade}  was added to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'{product.name} was added to your bag')
        else: 
            bag[item_id] = quantity
            messages.success(request, f'{product.name} was added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('bag-quantity'))
    shade = None
    if 'shade' in request.POST:
        shade = request.POST['shade']
    bag = request.session.get('bag', {})

    if shade:
        if quantity > 0:
            bag[item_id]['items_by_shade'][shade] = quantity
            messages.success(request, f'{product.name} - {shade} quantity was updated')
        else:
            del bag[item_id]['items_by_shade'][shade]
            messages.success(request, f'{product.name} - {shade} was removed from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} quantity was updated')

        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} was removed from your bag')


    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        shade = None
        if 'shade' in request.POST:
            shade = request.POST['shade']
        bag = request.session.get('bag', {})
        if shade:
            del bag[item_id]['items_by_shade'][shade]
            if not bag[item_id]['items_by_shade']:
                bag.pop(item_id)
                print('one')
                messages.success(request, f'{product.name} {shade} quantity was updated')

        else:
            bag.pop(item_id)
            print('two')
            messages.success(request, f'{product.name} was removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)