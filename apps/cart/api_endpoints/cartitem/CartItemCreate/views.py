from rest_framework import generics, status
from rest_framework.response import Response

from apps.cart.api_endpoints.cartitem.CartItemCreate.serializers import (
    CartItemCreateSerializer, CartItemCreateShortSerializer)
from apps.cart.models import CartItem
from apps.common.utils import get_cart
from apps.product.models import Product


class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemCreateShortSerializer
    queryset = CartItem.objects.all()

    """
    Create a cartitem with authenticated user or session_key.
    """

    def create(self, request, *args, **kwargs):
        cart = get_cart(request)
        request.data["cart"] = cart.id
        product = Product.objects.get(id=request.data['product'])
        if product.quantity >= 1:
            product.quantity -= 1
            product.save()
        else:
            raise Exception("Sorry, We have not this product.")
        serializer = CartItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["CartItemCreateAPIView"]
