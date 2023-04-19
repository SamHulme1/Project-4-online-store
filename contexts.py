from catalogue.models import Pricing, Product


def catagory_management(request):
    """context prossessor for accesssing the products
    and pricings across the site for the use on the promo banner
    and in the secondary navication"""
    promo = Pricing.objects.all()
    products_all = Product.objects.all()

    context = {
        "products_all": products_all,
        "promo": promo,
    }

    return context
