from django import forms
from .models import Listing


class CreateNewListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "product_image", "description",
                  "price", "quantity", "condition", "catagory")
