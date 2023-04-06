from django.db import models
from django.contrib.auth.models import User


class UserSetting(models.Model):
    """
    class for storing user settings allowing the user to manipulate
    how their store is displayed
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
