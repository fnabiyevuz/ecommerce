from rest_framework import serializers

from apps.order.models import Order


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "cart",
            "coupon",
            "total",
            "order_id",
            "full_name",
            "phone",
            "region",
            "district",
            "note",
            "status",
            "payment_type",
        )
