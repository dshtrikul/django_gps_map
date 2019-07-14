from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    address = forms.CharField(required=True, label='Address')

    class Meta:
        model = Address
        fields = ('address',)

# HIDDEN FORM GPS
