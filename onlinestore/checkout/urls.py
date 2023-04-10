from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import webhook

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('success/<order_number>', views.success, name="success"),
    path('cache_checkout_session/', views.cache_checkout_session, name="cache_checkout_session"),
    path('wh/', webhook, name='webhook'),
]