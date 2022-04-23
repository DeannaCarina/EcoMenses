from decimal import Decimal
from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    if product_count > 1:
        delivery = Decimal(product_count) + 2
    else:
        delivery = 0

    grand_total = total + delivery



    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context