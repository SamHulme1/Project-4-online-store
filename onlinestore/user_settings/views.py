from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserSetting
from .forms import UserSettingsForm


@login_required
def settings_view(request):
    return render(
            request, 'user_settings/my-settings.html')


@login_required
def create_settings(request):
    my_settings = UserSetting.objects.filter(user=request.user).first()
    if my_settings:
        return redirect(reverse('user_settings:edit_settings', args=[my_settings.id]))
    else:
        if request.method == 'POST':
            form = UserSettingsForm(request.POST, request.FILES)
            if form.is_valid():
                settings = form.save(commit=False)
                settings.user = request.user
                settings.save()
                messages.success(request, 'profile settings added') 
                return redirect(reverse('user_settings:settings_view'))
            else:
                messages.error(request, 'Your settings have not been updated')
        else:
            form = UserSettingsForm()
        return render(
            request, 'user_settings/create-settings.html', {"form": form})


@login_required
def edit_settings(request, id):
    settings = get_object_or_404(
        UserSetting, id=id)
    if request.method == 'POST':
        form = UserSettingsForm(
            request.POST, request.FILES, instance=settings)
        if form.is_valid():
            newSettings = form.save(commit=False)
            newSettings.user = request.user
            newSettings.save()
            messages.success(request, 'Settings updated') 
            return redirect(reverse('user_settings:settings_view'))
        else:
            messages.error(request, 'Your profile has not been updated')
    else:
        form = UserSettingsForm(instance=settings)
    context = {
        "form": form,
        'settings': settings
    }
    return render(
        request, 'user_settings/edit-settings.html', context)