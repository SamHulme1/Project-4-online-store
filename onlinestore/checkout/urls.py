from django.contrib import admin
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('success/<order_number>', views.success, name="success"),
]