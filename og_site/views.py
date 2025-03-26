from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
import stripe
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from octopusg import settings
from og_site.models import Product


def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def products(request):
    products = Product.objects.all().order_by('priority')
    template = loader.get_template('shop.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def buy_product(request, priority):
    product = get_object_or_404(Product, priority=priority)
    template = loader.get_template('buy_product.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))


def checkout_product(request, priority):
    product = get_object_or_404(Product, priority=priority)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),  # Convert price to cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )

        return redirect(session.url)

    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=400)


def success(request):
    return render(request, 'success.html', {'message': 'Payment was successful!'})


def cancel(request):
    return render(request, 'cancel.html', {'message': 'Payment was canceled.'})
