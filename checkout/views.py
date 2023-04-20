from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CustomerOrderForm
from basket.contexts import basket_contents
from catalogue.models import Pricing
from .models import OrderLineItem, Order
from user_profiles.models import UserInfo
from user_profiles.forms import UserInfoForm
from django.conf import settings
import stripe
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.core.mail import send_mail


@require_POST
def cache_checkout_session(request):
    """view for caching the checkout session in order to modify the stripe
    payment intent"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'save_info': request.POST.get('save_info'),
            'basket': json.dumps(request.session.get("basket", {})),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, 'Your payment cannot be processed'
                     'at the moment, sorry for any inconvinences')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """View for creating the checkiout takes the stipe payment keys
    gets the information on the user from the input form
    and the basket from the session uses the information
    provided to generate an order form for the user iterates
    through the items in the basket to create the stipe payment total"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_seceret_key = settings.STRIPE_SECRET_KEY
    profile = UserInfo.objects.filter(user=request.user).first()

    if request.method == "POST":
        basket = request.session.get('basket', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'address': request.POST['address'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        form = CustomerOrderForm(form_data, initial={
                "first_name": profile.d_first_name,
                "last_name": profile.d_last_name,
                'phone_number': profile.d_phone_number,
                'address': profile.d_address,
                'city': profile.d_city,
                'county': profile.d_county,
                'postcode': profile.d_postcode,
                'country': profile.d_country,
                 })
        if form.is_valid():
            order = form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    pricing = Pricing.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            pricing=pricing,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Pricing.DoesNotExist:
                    messages.error(
                        request, "an item in you basket is no longer avalible")
                    order.delete()
                    return redirect(reverse('basket:basket_view'))
            return redirect(
                reverse('checkout:success', args=[order.order_number]))
        else:
            messages.error(
                request, 'form error, make sure all fields are valid')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(
                request, "oops looks like there's nothing in your basket")
            return redirect(reverse('catalogue:all_products'))
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


@login_required
def success(request, order_number):
    """view for successful checkouts
    takes the order number as an argument
    gets the order generated
    if the user has a profile, gets the users info and
    saves the order to their profile, if the user hasnt created
    a profile yet, creates a new profile for them based uppon the
    data provided by them when they created an order saves the user
    to the profile and removes the basket from the session """
    basket = request.session.get('basket', {})
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserInfo.objects.filter(user=request.user).first()
        if profile:
            messages.success(
                request, "your order has been processed and is on you account")
            order.user_info = profile
            order.save()
        else:
            new_profile_data = {
                "d_first_name": order.first_name,
                "d_last_name": order.last_name,
                'd_email': order.email,
                'd_phone_number': order.phone_number,
                'd_address': order.address,
                'd_city': order.city,
                'd_county': order.county,
                'd_postcode': order.postcode,
                'd_country': order.country,
            }
            form = UserInfoForm(new_profile_data)
            if form.is_valid():
                new_profile = form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
                order.user_info = new_profile
                order.save()
                messages.success(
                    request, "your order has been processed,"
                             "a default account has been set up for you")

    messages.success(
        request, f"order created, your order number is {order.order_number}")
    send_mail(
        f"{order.order_number}",
        f"Your order for {order.order_total} was successful",
        settings.EMAIL_HOST_USER,
        [f"{order.email}"],
        fail_silently=False,
    )

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/success.html'
    context = {
        'order': order
    }

    return render(request, template, context)


def orders(request):
    """View for the user to see there orders, links on
    the page relate to the previous orders"""
    user = get_object_or_404(UserInfo, user=request.user)
    if user:
        previous_orders = Order.objects.filter(user_info=user.id)
    else:
        messages.error(
            request, 'You dont have any orders on your account')
        return (redirect(reverse("user_profiles:profile_view")))
    template = 'checkout/orders.html'
    context = {
        'previous_orders': previous_orders
    }

    return render(request, template, context)
