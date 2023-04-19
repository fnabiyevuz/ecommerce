from rest_framework import generics, status
from rest_framework.response import Response

from apps.cart.api_endpoints.cartitem.CartItemDelete.serializers import CartItemDeleteSerializer
from apps.cart.models import CartItem
from apps.common.utils import get_cart


class CartItemDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CartItemDeleteSerializer
    queryset = CartItem.objects.all()

    """
        Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        cart = get_cart(request)
        instance = self.get_object()
        if instance.cart == cart:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ["CartItemDeleteAPIView"]
