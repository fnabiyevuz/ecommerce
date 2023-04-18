from rest_framework import generics

from apps.wish.api_endpoints.wishlist.WishListCreate.serializers import WishListCreateSerializer
from apps.wish.models import WishList


class WishListCreateAPIView(generics.CreateAPIView):
    serializer_class = WishListCreateSerializer
    queryset = WishList.objects.all()


__all__ = ['WishListCreateAPIView']
