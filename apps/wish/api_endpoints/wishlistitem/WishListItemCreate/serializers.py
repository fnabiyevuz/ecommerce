from rest_framework import serializers

from apps.wish.models import WishListItem


class WishListItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = ('id', 'product', 'wishlist')
        # read_only_fields = ('wishlist',)
