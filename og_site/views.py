from django.http import HttpResponse
from django.template import loader
from og_site.models import Product

# class HomePageView(TemplateView):
#     model = Product
#     template_name = 'og_site/home.html'
#     context_object_name = 'products'

def products(request):
  products = Product.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))