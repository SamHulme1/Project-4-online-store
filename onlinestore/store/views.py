from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Listing
from django.contrib.auth.decorators import login_required
from .forms import CreateNewListing


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
def add_listing(request):
    if request.method == "POST":
        form = CreateNewListing(request.POST)
        if form.is_valid():
            listing = form.save()
        else:
            messages.error(request, 'listing not created'
                                    ' please ensure all form data is valid')

    else:
        form = CreateNewListing()

    template = 'store/add_listing.html'

    return render(request, template, {'form': form})
