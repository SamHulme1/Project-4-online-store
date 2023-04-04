from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import Listing


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        listed_product = get_object_or_404(
            Listing, pk=item_id, stock=Listing.Stock.AVALIBLE)
        total += quantity * listed_product.price
        product_count += quantity

        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'listed_product': listed_product
        })

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
