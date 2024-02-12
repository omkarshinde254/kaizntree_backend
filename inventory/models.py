from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.CharField(max_length=200)
    available = models.CharField(max_length=200)

    def __str__(self):
        return self.name

