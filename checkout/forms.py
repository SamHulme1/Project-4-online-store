from django import forms
from .models import Order


class CustomerOrderForm(forms.ModelForm):
    """form for creating an order"""
    class Meta:
        model = Order
        fields = ['first_name', 'last_name',"phone_number", 
                  "address", "county",
                  "postcode", "country",
                  'city', 'email']
