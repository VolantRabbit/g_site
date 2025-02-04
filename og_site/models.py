from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    priority = models.IntegerField(null=True, unique=True)

    def __str__(self):
        return self.name
