from rest_framework import serializers

from apps.order.models import Order


class OrderCreateWithCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "cart", "total", "coupon", "full_name", "phone", "region", "district", "note", "payment_type")


class OrderCreateSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField()

    class Meta:
        model = Order
        fields = ("id", "coupon", "session_key", "full_name", "phone", "region", "district", "note", "payment_type")
