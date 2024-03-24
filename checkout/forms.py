from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email Address',
        'phone': 'Phone Number',
        'street_address1': 'Street Address 1',
        'street_address2': 'Street Address 2',
        'town_or_city': 'Town or City',
        'county': 'County',
        'postcode': 'Postcode',
        'country': 'Country',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False