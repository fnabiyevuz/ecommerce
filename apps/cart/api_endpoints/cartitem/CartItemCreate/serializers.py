from rest_framework import serializers

from apps.cart.models import CartItem


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')
        # read_only_fields = ('wishlist',)
