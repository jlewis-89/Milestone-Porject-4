from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address1': 'Street Address 1',
            'address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'county': 'County, State or Locality',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
