from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserInfo(models.Model):
    """
    UserInfo model for storing infomation about the user
    in referance to their contact details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserSettings(models.Model):
    """
    class for storing user settings allowing the user to manipulate
    how their store is displayed
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', null=True)

    class BackgroundColour(models.Model):
        choices = (
            ("white", "white"),
            ("black", "black"),
            ("green", "green"),
            ("lightgray", "lightgray"),
            ("pink", "pink"),
            ("yellow", "yellow"),
        )
    store_background = models.CharField(
        choices=BackgroundColour.choices, default="white", max_length=15
    )

    def __str__(self):
        return str(self.user)
