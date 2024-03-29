from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserInfo
from user_settings.models import AccountSettings
from django.contrib.auth.decorators import login_required
from .forms import UserInfoForm


@login_required
def profile_view(request):
    user_settings = AccountSettings.objects.get(user=request.user)
    """"view for the profile home page"""

    context = {
        "user_settings": user_settings,
    }
    return render(
            request, 'user_profiles/my-profile.html', context)


@login_required
def create_profile_info(request):
    """view for creating a profile
    if a profile already exist with the same user which has a one to many
    relationship reverse to the edit profie view with the arguments of
    the users info id
    else render the create user info view which saves the new object and
    updates saves the user for the profile hidden user feild as the
    request user"""
    user_info = UserInfo.objects.filter(user=request.user).first()
    if user_info:
        return redirect(
            reverse('user_profiles:edit_profile_info', args=[user_info.id]))
    else:
        if request.method == 'POST':
            form = UserInfoForm(request.POST, request.FILES)
            if form.is_valid():
                info = form.save(commit=False)
                info.user = request.user
                info.save()
                messages.success(request, 'profile infomation updated')
                return redirect(reverse('user_profiles:profile_view'))
            else:
                messages.error(request, 'Your profile has not been updated')
        else:
            form = UserInfoForm()
        return render(
            request, 'user_profiles/create-profile-info.html', {"form": form})


@login_required
def edit_profile_info(request, id):
    """view for editing the users profile, same functionality
    as the create profile but with the instance as the retrieved user info
    object """
    usersInfomation = get_object_or_404(
        UserInfo, id=id)
    if request.method == 'POST':
        form = UserInfoForm(
            request.POST, request.FILES, instance=usersInfomation)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            messages.success(request, 'profile infomation updated')
            return redirect(reverse('user_profiles:profile_view'))
        else:
            messages.error(
                request, 'Your profile infomation has not been updated')
    else:
        form = UserInfoForm(instance=usersInfomation)
    context = {
        "form": form,
        'usersInfomation': usersInfomation
    }
    return render(
        request, 'user_profiles/edit-profile-info.html', context)
