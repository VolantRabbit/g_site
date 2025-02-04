from django.http import HttpResponse
from django.template import loader
from og_site.models import Product


def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def products(request):
    products = Product.objects.all()
    template = loader.get_template('shop.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def forum(request):
    template = loader.get_template('forum.html')
    return HttpResponse(template.render())
