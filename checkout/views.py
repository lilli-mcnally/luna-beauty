from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OabozL6ZsSlUMJa5744nSeTKReXCDFvQXbF3Re5ovLrTFlWwpLrsmOO5s85DDRKZ19JhwOlaaq1WaMmVf7SfYzU00saXpEP2g',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
