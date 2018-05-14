from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['customer_profile', 'commercial_group', 'zone', 'type', 'detail', 'mount', 'price', 'advance']
