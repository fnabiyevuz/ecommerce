from rest_framework import serializers

from apps.product.api_endpoints.DetailProduct.serializers import ProductDetailSerializer
from apps.product.models import Product


class RelatedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "image", "slug", "category", "description")

    def to_representation(self, instance):

        return ProductDetailSerializer(instance).data
