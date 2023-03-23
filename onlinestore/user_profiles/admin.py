from django.contrib import admin
from .models import UserInfo, UserSettings

admin.site.register(UserInfo)

admin.site.register(UserSettings)

# Register your models here.
