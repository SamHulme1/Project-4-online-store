from django.db import models
from django.contrib.auth.models import User


class UserSetting(models.Model):
    """
    class for storing user settings allowing the user to manipulate
    how the store is displayed
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class BackgroundColour(models.Model):
        choices = (
            ("dark-mode", "dark-mode"),
            ("light-mode", "light-mode"),
        )
    store_background = models.CharField(
        choices=BackgroundColour.choices, default="light-mode", max_length=15
    )

    def __str__(self):
        return str(self.user)
