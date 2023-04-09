from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CustomerOrderForm
from basket.contexts import basket_contents
from django.conf import settings
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_seceret_key = settings.STRIPE_SECRET_KEY
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

