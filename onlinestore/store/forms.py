from django import forms
from .models import Listing


class CreateNewListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
