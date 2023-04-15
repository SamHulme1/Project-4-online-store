from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserInfo(models.Model):
    """
    UserInfo model for storing infomation about the user
    in referance to their contact details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    d_first_name = models.CharField(max_length=150, null=True, blank=True)
    d_last_name = models.CharField(max_length=150, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    d_phone_number = models.CharField(max_length=20, null=True, blank=True)
    d_address = models.CharField(max_length=150, null=True, blank=True)
    d_city = models.CharField(max_length=40, null=True, blank=True)
    d_county = models.CharField(max_length=80, null=True, blank=True)
    d_postcode = models.CharField(max_length=20, null=True, blank=True)
    d_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username

