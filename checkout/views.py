from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KsCqLLKrlHsvpIcoIQGv0uU7w9IpD9D8k08kPswTwfx2M6P6wmN3jBsKUR7jwwR3kUhW8Xb0AJhIL5Kv7gFLIST00L7IPoNLB',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)