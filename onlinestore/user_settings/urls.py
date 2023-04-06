from django.urls import path
from . import views

app_name = 'user_settings'


urlpatterns = [
    path('', views.settings_view, name='settings_view'),
    path('create/', views.create_settings,
         name='create_settings'),
    path('edit/<int:id>/', views.edit_settings,
         name='edit_settings'),
]
