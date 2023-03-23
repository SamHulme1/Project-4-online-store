from django import forms
from .models import UserInfo, UserSettings


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ("phone_number", "address", "county",
                  "postcode", "country")


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = UserSettings
        fields = ("profile_picture", "store_background")