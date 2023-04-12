from django.urls import path
from . import views

app_name = 'user_profiles'


urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('create/', views.create_profile_info,
         name='create_profile_info'),
    path('edit/<int:id>/', views.edit_profile_info,
         name='edit_profile_info'),
]
