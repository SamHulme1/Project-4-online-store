from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ("d_phone_number", "d_address", "d_county",
                  "d_postcode", "d_country", 'd_first_name', 'd_last_name')
