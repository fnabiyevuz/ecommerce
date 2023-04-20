from rest_framework import serializers

from apps.order.models import Coupon


class CouponDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ("id", "code", "discount_type", "amount_discount", "min_amount", "is_available")
