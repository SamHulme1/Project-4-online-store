from catalogue.models import Pricing, Product


def catagory_management(request):
    pricing = Pricing.objects.all()
    products = Product.objects.all()

    context = {
        "products": products,
        "pricing": pricing,
    }

    return context
