from django.contrib import admin
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('pricings/', views.all_pricings, name='all_pricings'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('pricing_details/<int:id>', views.pricing_details, name='pricing_details'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_pricing/', views.add_pricing, name='add_pricing'),
    path('saved/', views.get_favourite, name="get_favourite"),
    path('search/', views.search_results, name="search_results"),
    path('catagory/<str:cat>', views.catagory, name="catagory"),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('fav/<int:id>', views.favourite_product, name='favourite_product'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('edit_pricing/<int:id>', views.edit_pricing, name='edit_pricing')
]
