from django.urls import path
from . import views, forum_views
from .forum_views import ThreadList, ThreadCreate, ThreadDetail, PostCreate

urlpatterns = [
    path('', views.main, name='home'),
    path('products/', views.products, name='products'),
    path('buy/<int:priority>/', views.buy_product, name='buy_product'),
    path('checkout/<int:priority>/', views.checkout_product, name='checkout_product'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),

    path('forum/', ThreadList.as_view(), name='forum'),
    path('forum/new/', ThreadCreate.as_view(), name='thread_create'),
    path('forum/thread/<int:pk>/', ThreadDetail.as_view(), name='thread_detail'),
    path('forum/thread/<int:pk>/reply/', PostCreate.as_view(), name='post_create'),
]
