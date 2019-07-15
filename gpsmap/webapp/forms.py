from django import forms
from .models import Address, Files

class AddressForm(forms.ModelForm):
    address = forms.CharField(required=False, label='Address')

    class Meta:
        model = Address
        fields = ('address',)

class FileForm(forms.ModelForm):
    txtfile = forms.FileField(required=False, label=' ')

    class Meta:
        model = Files
        fields = ('txtfile',)
