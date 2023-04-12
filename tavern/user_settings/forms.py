from django import forms
from .models import UserSetting


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = UserSetting
        fields = ("store_background",)
