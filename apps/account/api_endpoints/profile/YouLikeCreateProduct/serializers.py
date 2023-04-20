from rest_framework import serializers

from apps.account.models import YouLikeProduct
from apps.product.api_endpoints.ListProduct.serializers import ProductListSerializer


class YouLikeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLikeProduct
        fields = ("user",)

    def validate(self, attrs):
        product = attrs.get("product")
        user = attrs.get("user")
        if YouLikeProduct.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("You already liked this product")
        return attrs
