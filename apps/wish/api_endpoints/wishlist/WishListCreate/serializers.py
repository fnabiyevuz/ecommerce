from rest_framework import serializers

from apps.wish.models import WishList


class WishListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'user', 'session_key')