from rest_framework import serializers

from apps.product.models import Product


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "price",
            "image",
            "description",
            "quantity",
            "rating",
            "currency",
            "discount_price",
            "type",
            "material",
            "design",
            "customization",
            "protection",
            "warranty",
            "supplier",
            "manufacturer",
            "brand",
            "company",
            "condition",
            "view_count",
        )
