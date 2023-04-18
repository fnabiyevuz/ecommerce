from rest_framework import serializers

from apps.wish.models import WishListItem


class WishListItemDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = ('id', 'product', 'wishlist')
