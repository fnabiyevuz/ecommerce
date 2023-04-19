from rest_framework import generics, status
from rest_framework.response import Response

from apps.cart.api_endpoints.cartitem.CartItemCreate.serializers import \
    CartItemCreateSerializer
from apps.cart.choices import CartStatusType
from apps.cart.models import Cart, CartItem
from apps.common.utils import get_session_key


class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemCreateSerializer
    queryset = CartItem.objects.all()

    """
    Create a cartitem with authenticated user or session_key.
    """

    def create(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user, status=CartStatusType.NEW)
        else:
            cart, _ = Cart.objects.get_or_create(session_key=get_session_key(request))
        request.data["cart"] = cart.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["CartItemCreateAPIView"]
