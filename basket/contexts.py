from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    
    if product_count >= 11:
        delivery_cost = 12
    elif product_count >= 1 & product_count <= 10:
        delivery_cost = Decimal(product_count) + 2
    else:
        delivery_cost = 0

    grand_total = total + delivery_cost



    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context