from rest_framework import serializers

from apps.cart.models import Cart


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("id", "status")
