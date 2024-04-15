from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
        'default_name': 'Name',
        'default_phone': 'Phone Number',
        'default_street_address1': 'Street Address 1',
        'default_street_address2': 'Street Address 2',
        'default_town_or_city': 'Town or City',
        'default_county': 'County',
        'default_postcode': 'Postcode',
        }

        self.fields['default_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False