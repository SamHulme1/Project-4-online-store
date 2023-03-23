from django.urls import path
from . import views

app_name = 'user_profiles'


urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('settings/', views.profile_settings,
         name='profile_settings'),
    path('info/', views.profile_info,
         name='profile_info')
]
