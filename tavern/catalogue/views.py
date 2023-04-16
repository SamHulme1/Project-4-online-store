from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Pricing, Product
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CreateNewProduct, CreateNewPricing
from django.db.models import Q


def catagory(request, cat):
    catagories = Product.objects.filter(catagory=cat)
    return render(request, "catalogue/catagories.html", {
        "cat": cat, "catagories": catagories})


def search_results(request):
    if request.method == "GET":
        searched = request.GET["searched"]
        results = Product.objects.filter(Q(title__icontains=searched) |
                                         Q(description__icontains=searched))
        return render(request, 'catalogue/search.html', {
            "searched": searched, "results": results})
    else:
        return render(request, 'catalogue/search.html', {})


def all_pricings(request):
    pricings = Pricing.objects.all()
    return render(request, 'catalogue/pricings.html', {
        'pricings': pricings})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'catalogue/products.html', {
        'products': products})


def product_details(request, id):
    # I used https://www.youtube.com/watch?v=1XiJvIuvqhs&t=653s
    # to help me build the favourites part
    favourite = False
    product = get_object_or_404(Product, id=id)
    if product.favourite.filter(id=request.user.id).exists():
        favourite = True
    context = {
        "product": product,
        "favourite": favourite
    }
    return render(request, 'catalogue/product_details.html', context)


def pricing_details(request, id):
    pricing = get_object_or_404(Pricing, id=id)
    products = Product.objects.all()
    product_catagory = products.filter(catagory=pricing.title)
    context = {
        "pricing": pricing,
        "products": products,
        "product_catagory": product_catagory,
    }
    return render(request, 'catalogue/pricing_details.html', context)


@login_required
def get_favourite(request):
    user = request.user
    favourite = user.favourite.all()
    return render(request, 'catalogue/favourites.html', {
        'favourite': favourite})


@staff_member_required
def add_product(request):
    if request.method == "POST":
        form = CreateNewProduct(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            messages.success(request, 'product created successfully')
            return redirect(reverse('catalogue:all_products'))
        else:
            messages.error(request, 'product not created'
                                    ' please ensure all form data is valid')

    else:
        form = CreateNewProduct()

    template = 'catalogue/add_product.html'

    return render(request, template, {'form': form})


@staff_member_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user.is_staff:
        messages.success(
            request, f'{request.user} {product.title} has been deleted')
        product.delete()
    else:
        messages.error(
            request,
            f"{request.user} only staff can delte products!")
    return redirect(reverse('catalogue:all_products'))


@staff_member_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = CreateNewProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'product updated successfully')
            return redirect(reverse('catalogue:all_products'))
        else:
            messages.error(request, 'product not updated'
                                    ' please ensure all form data is valid')
    else:
        form = CreateNewProduct(instance=product)
        messages.info(
            request, f"{request.user} you're editing product {product.title}")

    template = 'catalogue/edit_product.html'
    context = {
        'form': form,
        "product": product
    }

    return render(request, template, context)


@staff_member_required
def add_pricing(request):
    if request.method == "POST":
        form = CreateNewPricing(request.POST, request.FILES)
        if form.is_valid():
            new_pricing = form.save()
            messages.success(request, 'pricing created successfully')
            return redirect(reverse('catalogue:all_products'))
        else:
            messages.error(request, 'pricing not created'
                                    ' please ensure all form data is valid')

    else:
        form = CreateNewPricing()

    template = 'catalogue/add_pricing.html'

    return render(request, template, {'form': form})


@staff_member_required
def delete_pricing(request, id):
    pricing = get_object_or_404(Pricing, id=id)
    if request.user.is_staff:
        messages.success(
            request, f'{request.user} {pricing.title} deleted')
        pricing.delete()
    else:
        messages.error(
            request,
            f"{request.user} only staff can delte pricings!")
    return redirect(reverse('catalogue:all_products'))


@staff_member_required
def edit_pricing(request, id):
    pricing = get_object_or_404(Pricing, id=id)
    if request.method == "POST":
        form = CreateNewPricing(request.POST, request.FILES, instance=pricing)
        if form.is_valid():
            pricing = form.save()
            messages.success(request, 'pricing updated successfully')
            return redirect(reverse('catalog:all_products'))
        else:
            messages.error(request, 'pricing not updated'
                                    ' please ensure all form data is valid')
    else:
        form = CreateNewPricing(instance=pricing)
        messages.info(
            request, f"{request.user} you're editing pricing {pricing.title}")

    template = 'catalogue/edit_pricing.html'
    context = {
        'form': form,
        "pricing": pricing
    }

    return render(request, template, context)


@login_required
def favourite_product(request, id):
    product = get_object_or_404(Product, id=id)
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        messages.success(request, "product unfavourited")
    else:
        product.favourite.add(request.user)
        messages.success(request, "product favourited")
    return redirect(reverse("catalogue:product_details", args=[product.id]))
