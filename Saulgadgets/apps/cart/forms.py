from django.forms import ModelForm, fields
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model =Payment
        fields =("amount","email","phone_number", "full_name")


