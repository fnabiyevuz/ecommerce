from rest_framework import serializers
from apps.account.models import YouLikeProduct


class YouLikeProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLikeProduct
        fields = ("product",)