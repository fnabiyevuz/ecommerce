from rest_framework import serializers

from apps.cart.models import CartItem
from apps.product.models import Product


class ProductShortCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "image", "rating", "currency", "price", "discount_price", "brand")


class CartItemListSerializer(serializers.ModelSerializer):
    product = ProductShortCartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ("id", "product", "quantity", "price")
