from rest_framework import serializers

from apps.product.models import Product
from apps.wish.models import WishListItem


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'rating', 'currency', 'price', 'discount_price', 'brand')


class WishListItemListSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer(read_only=True)

    class Meta:
        model = WishListItem
        fields = ('id', 'product')
