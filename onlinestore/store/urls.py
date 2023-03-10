from django.contrib import admin
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_listings, name='all_listings'), 
    path('<int:id>/', views.listing_details, name='listing_details'),
]