from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from catalogue.models import Pricing
from django.contrib.auth.decorators import login_required


@login_required
def basket_view(request):
    """view for the users basket only avalible to those signed in"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """add to basket fuctionality
    stores the quantity of the items in the users basket
    gets this information from the add to basket button in post
    gets the current basket from the session
    if the item is in the basket list adjust the quantity by 1
    return the user to the current page after the action"""
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
    """change basket functionality
    get the curent quantity of the basket whenever the
    quantity is changed
    if the basket has items with the quantity of 0 remove the
    item from the basket the set the basket equal to the basket
    after modifications and returnn the user to the basket page
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity == 0:
        basket.pop(item_id)
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(reverse('basket:basket_view'))
