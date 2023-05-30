from django.urls import path
from . import views

app_name = 'user_settings'


urlpatterns = [
    path('', views.settings_view, name='settings_view'),
    path('dark/', views.set_dark_mode, name='set_dark_mode'),
    path('fonts/', views.set_larger_fonts_mode, name='set_larger_fonts_mode'),
]
