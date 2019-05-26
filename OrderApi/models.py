from django.db import models

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = (
        ('CANCEL', 'Cancelled'),
        ('COMPLETE', 'Completed'),
        ('SHIP', 'Shipped'),
        ('PAY', 'Paid'),
    )

    date = models.DateField(auto_now_add=True)
    productId = models.IntegerField()
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ORDER_STATUS)
    
# class OrderStatusChangedMessage(models.Model):
#     pass
