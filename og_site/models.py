from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    priority = models.IntegerField(null=True, unique=True)

    def __str__(self):
        return self.name


class DataTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Thread(DataTime):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(DataTime):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()

    def __str__(self):
        return f"Post by {self.created_by} in {self.thread.title}"
