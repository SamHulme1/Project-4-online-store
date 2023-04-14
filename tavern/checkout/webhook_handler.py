from django.http import HttpResponse
from .models import Order, OrderLineItem
from catalogue.models import Pricing

import json
import time


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        full_name = billing_details.name.split()
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt < 6:
            try:
                order = Order.objects.get(
                    first_name=full_name[0],
                    last_name=full_name[1],
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.address.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address__iexact=shipping_details.address.line1,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | SUCCESS: order has been verified',
                    status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=full_name[0],
                    last_name=full_name[1],
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.address.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address__iexact=shipping_details.address.line1,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                    )
                pricing = Pricing.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        pricing=pricing,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                                    status=500)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]} | SUCCESS: webhook created order',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)