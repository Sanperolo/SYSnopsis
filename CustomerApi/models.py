from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.IntegerField()
    billingAddress = models.TextField()
    shippingAddress = models.TextField()
    creditStanding = models.DecimalField(max_digits=30, decimal_places=15)
