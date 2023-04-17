from django import forms
from .models import Pricing, Product


choices = Pricing.objects.all().values_list("title", "title")

catagory_list = []

for catagory in choices:
    catagory_list.append(catagory)


class CreateNewPricing(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ["title", "price", 'promo_image']


class CreateNewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "product_image", "description", "catagory"]

        widgets = {
            "catagory": forms.Select(
                choices=catagory_list, attrs={"class": "form-control"})
        }
