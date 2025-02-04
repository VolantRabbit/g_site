from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('products/', views.products, name='products'),
    path('forum/', views.forum, name='forum'),
]
