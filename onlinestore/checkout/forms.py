from django import forms
from .models import Order


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["phone_number", "address", "county",
                  "postcode", "country", 'first_name', 'last_name']