from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import AccountSettings
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def settings_view(request):
    dark_mode = False
    larger_fonts = False
    return render(
            request, 'user_settings/users_settings.html')


def set_dark_mode(request):
    user_settings = AccountSettings.objects.get(user=request.user)
    if user_settings.dark_mode is False:
        user_settings.dark_mode = True
        user_settings.save()
        request.session['dark_mode'] = True
    else:
        user_settings.dark_mode = False
        user_settings.save()
        request.session['dark_mode'] = False

    return redirect(reverse("user_profiles:profile_view"))


def set_larger_fonts_mode(request):
    user_settings = AccountSettings.objects.get(user=request.user)
    if user_settings.larger_fonts is False:
        user_settings.larger_fonts = True
        user_settings.save()
    else:
        user_settings.larger_fonts = False
        user_settings.save()
    
    return redirect(reverse("user_profiles:profile_view"))
