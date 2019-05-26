from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=30, decimal_places=15)
    itemInStock = models.IntegerField()
    itemReserved = models.IntegerField()
