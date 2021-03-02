from django import forms

class AddressForm(forms.Form):
    CHOICES = (('Option 1', 'Address 1'),('Option 2', 'Address 2'),)
    Address = forms.ChoiceField(choices=CHOICES)