from rest_framework import serializers

from apps.account.models import Account, YouLikeProduct
from apps.product.api_endpoints.ListProduct.serializers import ProductListSerializer
from apps.product.models import Product


class YouLikeProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLikeProduct
        fields = ("id", "product")

    def get_product(self, obj):
        product = obj.product
        return ProductListSerializer(product).data
