from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_view, name='basket_view'), 
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path(
        'adjust/<item_id>/', views.change_basket_qty, name='change_basket_qty')
]