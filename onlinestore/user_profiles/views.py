from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserInfo, UserSettings
from django.contrib.auth.decorators import login_required
from .forms import UserInfoForm, UserSettingsForm


@login_required
def profile_view(request):
    user_infomation = UserInfo.objects.filter(user=request.user.id)
    return render(
            request, 'my-profile.html', {'user_infomation': user_infomation})


@login_required
def profile_info(request):
    user = request.user
    users_profile = UserInfo.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            if users_profile:
                users_profile.delete()
                info = form.save()
                info.user = user
                info.save()
                messages.success(request, 'Settings updated')
            else:
                info = form.save()
                info.user = user
                info.save()
                messages.success(request, 'Settings updated')
            messages.success(request, 'Profile updated')
        else:
            messages.error(request, 'Your profile has not been updated')
    else:
        form = UserInfoForm()
    return render(
        request, 'create-profile-info.html', {"form": form})


@login_required
def profile_settings(request):
    user = request.user
    users_settings = UserSettings.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, request.FILES)
        if form.is_valid():
            if users_settings:
                users_settings.delete()
                settings = form.save()
                settings.user = user
                settings.save()
                messages.success(request, 'Settings updated')
            else:
                settings = form.save()
                settings.user = user
                settings.save()
                messages.success(request, 'Settings updated')
            return redirect('store:get_sellers_listings')
        else:
            messages.error(request, 'Settings have not been updated')
    else:
        form = UserSettingsForm()

    return render(
        request, 'profile-settings.html', {'form': form})
