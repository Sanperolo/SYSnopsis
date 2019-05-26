from .models import Order, OrderStatusChangedMessage
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('date', 'productId', 'quantity', 'name', 'status')


# class OrderStatusSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = OrderStatusChangedMessage
#         fields = ('url', 'name')