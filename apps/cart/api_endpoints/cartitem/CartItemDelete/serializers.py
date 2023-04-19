from rest_framework import serializers

from apps.cart.models import CartItem


class CartItemDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product')
