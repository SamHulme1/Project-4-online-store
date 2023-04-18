from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Pricing, Product
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CreateNewProduct, CreateNewPricing
from django.db.models import Q


def catagory(request, cat):
    """view for getting the catagory of a product
    I used a tutorial to help me build this view,
    https://www.youtube.com/watch?v=PTsljbR-Cmo"""
    catagories = Product.objects.filter(catagory_name=cat)
    return render(request, "catalogue/catagories.html", {
        "cat": cat, "catagories": catagories})


def search_results(request):
    """view starts by getting the search results from the users input
    then uses a query to filters the product objects in the db
    that have the title or description of the search request
    Finishes by returning the user to the catagory page and
    showing them the results
    of all products in there search,
    if te results are empty the page will show no results"""
    if request.method == "GET":
        searched = request.GET["searched"]
        results = Product.objects.filter(Q(title__icontains=searched) |
                                         Q(description__icontains=searched))
        return render(request, 'catalogue/search.html', {
            "searched": searched, "results": results})
    else:
        return render(request, 'catalogue/search.html')


def all_pricings(request):
    """ Veiw for getting all of the pricing boxes in the catalogue"""
    pricings = Pricing.objects.all()
    return render(request, 'catalogue/pricings.html', {
        'pricings': pricings})


def all_products(request):
    """Veiw for getting all of the products in the catalogue"""
    products = Product.objects.all()
    return render(request, 'catalogue/products.html', {
        'products': products})


def product_details(request, id):
    """Veiw for rendering the product details of a product in the store
    if the product is favourited by the user, set the value of favourite from
    false to true
    I used https://www.youtube.com/watch?v=1XiJvIuvqhs&t=653s
    to help me build the favourites part
    """
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
    """ This view is similar to the product details,
    however this one also takes the context of products and product
    catagory defined below, the product is just a simple query to
    get all the products, whereas the catagory is a filter method
    used after getting the products to filter if the product catagory
    name is the same as the pricing title
    if so the products render in a drop down button the the html
    to provide a convient way for the user to view which products are
    in which box"""
    pricing = get_object_or_404(Pricing, id=id)
    products = Product.objects.all()
    product_catagory = products.filter(catagory_name=pricing.title)
    context = {
        "pricing": pricing,
        "products": products,
        "product_catagory": product_catagory,
    }
    return render(request, 'catalogue/pricing_details.html', context)


@login_required
def get_favourite(request):
    """view for getting all the products that contain the
    manytomany key on the model
    based upon the user """
    user = request.user
    favourite = user.favourite.all()
    return render(request, 'catalogue/favourites.html', {
        'favourite': favourite})


@staff_member_required
def add_product(request):
    """view for adding a product to the catalogue
    the when a user creates a product the and submits the form
    change the hidden catagory name field to be a stringified version
    of the product catagory foren key, view is
    protected by a staff member decorator
    to stop regular users from adding products"""
    if request.method == "POST":
        form = CreateNewProduct(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.catagory_name = str(new_product.catagory)
            new_product.save()
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
    """veiw deleting a product from the
    store conditional check to see if the user
    is authenticated as an extra precaution
    even though the url is already secured
    through the staff member decorator"""
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
    """view for editing a product, this view is the same as
    the add products veiw but it takes the instance of product so the
    db knows which instance it is updating """
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = CreateNewProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            product.catagory_name = str(product.catagory)
            product.save()
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
    """view for adding a pricing to the store the same
    functionality as the add product, however without the additional save"""
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
    """ view for deleting a pricig from the store same functionality as
    the delete product"""
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
    """view for edting a pricing, the same functionality as ediitng products
    but for a differnet model"""
    pricing = get_object_or_404(Pricing, id=id)
    if request.method == "POST":
        form = CreateNewPricing(request.POST, request.FILES, instance=pricing)
        if form.is_valid():
            pricing = form.save()
            messages.success(request, 'pricing updated successfully')
            return redirect(reverse('catalogue:all_products'))
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
    """ this view is for when a user favourites a product, it starts by getting
    a product and then checking if it is already a favourite
    after the user clicks the url if it is favourited it changes the status of
    favourite for that user on the model from true to false and vise versa
    displaying messages when they are updated
    finally the view returns a reverse back to the product details page
    taking the arguments of that products id"""
    product = get_object_or_404(Product, id=id)
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        messages.success(request, "product unfavourited")
    else:
        product.favourite.add(request.user)
        messages.success(request, "product favourited")
    return redirect(reverse("catalogue:product_details", args=[product.id]))
