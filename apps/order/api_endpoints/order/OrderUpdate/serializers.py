from rest_framework import serializers

from apps.order.models import Order


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "full_name", "phone", "region", "district", "note", "status", "payment_type")
