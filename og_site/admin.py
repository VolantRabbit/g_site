from django.contrib import admin
from .models import Product, Thread, Post


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Thread)
admin.site.register(Post)
