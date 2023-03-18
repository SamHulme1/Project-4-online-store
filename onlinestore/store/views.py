from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Listing
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
    sellers_listings = Listing.avalible.all()
    return render(request, 'store/sellers_listings.html', {
        'sellers_listings': sellers_listings})


def all_listings(request):
    listings = Listing.avalible.all()
    return render(request, 'store/listings.html', {
        'listings': listings})


def listing_details(request, id):
    listing_details = get_object_or_404(
        Listing, id=id, stock=Listing.Stock.AVALIBLE)
    return render(request, 'store/listing_details.html', {
        'listing_details': listing_details})


@login_required
def get_favourite(request):
    listing_favourites = Listing.objects.filter(favourites=1)
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
        else:
            messages.error(request, 'listing not created'
                                    ' please ensure all form data is valid')

    else:
        form = CreateNewListing()

    template = 'store/add_listing.html'

    return render(request, template, {'form': form})
