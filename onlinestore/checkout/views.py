from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CustomerOrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error("oops looks like there's nothing in your basket")
        return redirect(reverse('store:all_listings'))

    form = CustomerOrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form': form
    }

    return render(request, template, context)

