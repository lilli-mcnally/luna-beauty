from django.shortcuts import render

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    template = 'profiles/profile.html'
    context = {}

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders
    }

    return render(request, template, context)
