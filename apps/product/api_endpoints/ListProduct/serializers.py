from rest_framework import serializers

from apps.product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "category", "price", "description", "image")
