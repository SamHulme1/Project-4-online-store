from catalogue.models import Pricing, Product


def catagory_management(request):
    promo = Pricing.objects.all()
    products_all = Product.objects.all()

    context = {
        "products_all": products_all,
        "promo": promo,
    }

    return context
