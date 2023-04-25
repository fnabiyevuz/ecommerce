from rest_framework import generics

from apps.cart.api_endpoints.cart.CartDetail.serializers import CartDetailSerializer
from apps.cart.models import Cart


class CartDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()


__all__ = ["CartDetailAPIView"]
