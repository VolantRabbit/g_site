from django.urls import path
from . import views, forum_views
from .forum_views import ThreadListView

urlpatterns = [
    path('', views.main, name='home'),
    path('products/', views.products, name='products'),
    path('buy/<int:priority>/', views.buy_product, name='buy_product'),
    path('checkout/<int:priority>/', views.checkout_product, name='checkout_product'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    # path('forum/', forum_views.forum, name='forum'),
    path('forum/', ThreadListView.as_view(), name='forum'),
]
