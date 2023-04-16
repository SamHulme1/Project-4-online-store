from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from catalogue.models import Pricing
from django.contrib.auth.decorators import login_required


@login_required
def basket_view(request):
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    pricing = get_object_or_404(Pricing, id=item_id)

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f"{pricing.title} added to basket")
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def change_basket_qty(request, item_id):
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity == 0:
        basket.pop(item_id)
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(reverse('basket:basket_view'))

