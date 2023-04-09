from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import CustomerOrderForm
from basket.contexts import basket_contents
from store.models import Listing
from .models import OrderLineItem, Order
from django.conf import settings
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_seceret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['first_name'],
            'address': request.POST['address'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        form = CustomerOrderForm(form_data)
        if form.is_valid:
            order = form.save()
            for item_id, item_data in basket.items():
                try:
                    listing = Listing.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            listing=listing,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Listing.DoesNotExist:
                    messages.error(request, "an item in you basket is no longer avalible")
                    order.delete()
                    return redirect(reverse('basket:basket_view'))
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('checkout:success', args=[order.order_number]))
        else:
            messages.error(request, 'form error, make sure all fields are valid')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error("oops looks like there's nothing in your basket")
            return redirect(reverse('store:all_listings'))
        current_basket = basket_contents(request)
        current_basket_total = current_basket['grand_total']
        stripe_total = round(current_basket_total * 100)
        stripe.api_key = stripe_seceret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        form = CustomerOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)


def success(request, order_number):
    basket = request.session.get('basket', {})
    safe_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    basket.clear()

    template = 'checkout/success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
