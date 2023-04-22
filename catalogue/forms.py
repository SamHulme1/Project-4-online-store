from django import forms
from .models import Pricing, Product


choices = Pricing.objects.all().values_list("title", "title")

catagory_list = []


class CreateNewPricing(forms.ModelForm):
    """form for creating a new pricing box"""
    class Meta:
        model = Pricing
        fields = ["title", "price", 'promo_image']


class CreateNewProduct(forms.ModelForm):
    """ form for creating a new product
    form catagory select comes from the list above
    I used this tutorial to help build this fuctionality
    its the same one referenced in the view docstrig for catagory
    https://www.youtube.com/watch?v=PTsljbR-Cmo"""
    class Meta:
        model = Product
        fields = ["title", "product_image", "description", "catagory"]

        widgets = {
            "catagory": forms.Select(
                choices=catagory_list, attrs={"class": "form-control"})
        }
