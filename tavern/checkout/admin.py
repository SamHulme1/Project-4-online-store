from django.contrib import admin

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name',
                    'order_total', 'delivery_cost',
                    'grand_total',
                    'created', 'last_name']

    readonly_fields = ['order_number', 'created',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket', 
                       'stripe_pid']

    fields = ['order_number', 'user_info', 'first_name',
              'last_name', 'email', 'address', 'city',
              'county', 'postcode', 'country',
              'created',
              'delivery_cost', 'order_total',
              'grand_total', 'original_basket',
              'stripe_pid']

    list_filter = ['created']

    inlines = [OrderLineItemAdminInline]
# Register your models here.
