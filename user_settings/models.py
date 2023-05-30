from django.db import models
from django.contrib.auth.models import User


class AccountSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dark_mode = models.BooleanField()
    larger_fonts = models.BooleanField()

    def __str__(self):
        return self.user.username
