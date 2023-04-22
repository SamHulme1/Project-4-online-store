from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):
    """form for creating a profile, the d represents default"""
    class Meta:
        model = UserInfo
        fields = ['d_first_name', 'd_last_name', "d_phone_number", "d_address",
                  "d_county", 'd_city', "d_postcode", "d_country",]
