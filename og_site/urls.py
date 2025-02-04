from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('products/', views.products, name='products'),
    path('forum/', views.forum, name='forum'),
    path('buy/<int:priority>/', views.buy_product, name='buy_product'),
    path('checkout/<int:priority>/', views.checkout_product, name='checkout_product'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
