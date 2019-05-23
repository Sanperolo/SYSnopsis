from django.db import models

# Create your models here.
class Product(models.Model)
    name = models.CharField()
    price = models.DecimalField()
    itemInStock = models.IntegerField()
    itemReserved = models.IntegerField()
    