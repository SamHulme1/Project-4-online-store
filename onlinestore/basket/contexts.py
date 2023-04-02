from decimal import Decimal
from django.conf import settings


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0

    delivery_price = total * Decimal(
        settings.STANDARD_DELEVERY_PERCENTAGE / 100)

    grand_total = total + delivery_price
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery_price': delivery_price,
        'grand_total': grand_total
    }

    return context
