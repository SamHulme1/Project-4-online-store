from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Listing
from user_settings.models import UserSetting
from django.contrib.auth.decorators import login_required
from .forms import CreateNewListing
from django.db.models import Q


def catagory(request, cat):
    listing_catagories = Listing.objects.filter(catagory=cat)
    return render(request, "store/catagories.html", {
        "cat": cat, "listing_catagories": listing_catagories})


def search_results(request):
    if request.method == "GET":
        searched = request.GET["searched"]
        results = Listing.objects.filter(Q(title__icontains=searched) |
                                         Q(description__icontains=searched))
        return render(request, 'store/search.html', {
            "searched": searched, "results": results})
    else:
        return render(request, 'store/search.html', {})


def get_sellers_listings(request):
    sellers_listings = Listing.objects.all()
    seller_settings = UserSettings.objects.filter(user=request.user)
    return render(request, 'store/sellers_listings.html', {
        'sellers_listings': sellers_listings,
        'seller_settings': seller_settings})


def all_listings(request):
    listings = Listing.avalible.all()
    return render(request, 'store/listings.html', {
        'listings': listings})


def listing_details(request, id):
    # I used https://www.youtube.com/watch?v=1XiJvIuvqhs&t=653s
    # to help me build the favourites part
    favourite = False
    listing = get_object_or_404(
        Listing, id=id, stock=Listing.Stock.AVALIBLE)
    if listing.favourite.filter(id=request.user.id).exists():
        favourite = True
    context = {
        "listing": listing,
        "favourite": favourite
    }
    return render(request, 'store/listing_details.html', context)


@login_required
def get_favourite(request):
    user = request.user
    listing_favourites = user.favourite.all()
    return render(request, 'store/listing_favourites.html', {
        'listing_favourites': listing_favourites})


@login_required
def add_listing(request):
    user = request.user
    if request.method == "POST":
        form = CreateNewListing(request.POST, request.FILES)
        if form.is_valid():
            new_listing = form.save()
            new_listing.sellerID = user
            new_listing.save()
            messages.success(request, 'listing created successfully')
            return redirect(reverse('store:get_sellers_listings'))
        else:
            messages.error(request, 'listing not created'
                                    ' please ensure all form data is valid')

    else:
        form = CreateNewListing()

    template = 'store/add_listing.html'

    return render(request, template, {'form': form})


@login_required
def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.user == listing.sellerID:
        messages.success(
            request, f'{request.user} your listing has been deleted')
        listing.delete()
    else:
        messages.error(
            request,
            f"{request.user} this is not your listing! You can't delete it!")
    return redirect(reverse('store:get_sellers_listings'))


@login_required
def edit_listing(request, id):
    user = request.user
    listing = get_object_or_404(Listing, id=id)
    if request.user != listing.sellerID:
        messages.error(
            request,
            f"{user} this is not your listing! You can't change it!")
        return redirect(reverse('store:get_sellers_listings'))

    if request.method == "POST":
        form = CreateNewListing(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()
            listing.sellerID = user
            listing.save()
            messages.success(request, 'listing updated successfully')
            return redirect(reverse('store:get_sellers_listings'))
        else:
            messages.error(request, 'listing not updated'
                                    ' please ensure all form data is valid')

    else:
        form = CreateNewListing(instance=listing)
        messages.info(
            request, f"{user} you're editing your listing {listing.title}")

    template = 'store/edit_listing.html'
    context = {
        'form': form,
        "listing": listing
    }

    return render(request, template, context)


@login_required
def favourite_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    if listing.favourite.filter(id=request.user.id).exists():
        listing.favourite.remove(request.user)
        messages.success(request, "Listing unfavourited")
    else:
        listing.favourite.add(request.user)
        messages.success(request, "Listing favourited")
    return redirect(reverse("store:listing_details", args=[listing.id]))
