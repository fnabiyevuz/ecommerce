from rest_framework import serializers

from apps.account.models import Account
from apps.order.models import Order, OrderStatusType
from apps.product.models import Review


class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "user", "product", "desc", "status", "ip", "rating")
