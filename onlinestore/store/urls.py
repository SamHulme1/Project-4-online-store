from django.contrib import admin
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_listings, name='all_listings'),
    path('seller/', views.get_sellers_listings, name='get_sellers_listings'),
    path('<int:id>/', views.listing_details, name='listing_details'),
    path('add/', views.add_listing, name='add_listing'),
    path('saved/', views.get_favourite, name="get_favourite"),
    path('search/', views.search_results, name="search_results"),
    path('catagory/<str:cat>', views.catagory, name="catagory")
]
