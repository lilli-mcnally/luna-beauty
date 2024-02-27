from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    shade = None
    if 'shade' in request.POST:
        shade = request.POST['shade']

    bag = request.session.get('bag', {})

    if shade:
        if item_id in list(bag.keys()):
            print(bag[item_id])
            if shade in bag[item_id]['items_by_shade'].keys():
                bag[item_id]['items_by_shade'][shade] += quantity
            else:
                print(bag[item_id])
                bag[item_id]['items_by_shade'][shade] = quantity
        else:
            bag[item_id] = {'items_by_shade': {shade: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else: 
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
