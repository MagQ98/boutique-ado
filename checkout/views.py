from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K6f6ADBRKWE3Pff3n5DMGSqulnBav6Okjh4YZweRaj0MRdRxGGnzPRFG7nVaG1iurNGZ1J3Qw0GkORjFSq5p8cg00riAMobKP',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
