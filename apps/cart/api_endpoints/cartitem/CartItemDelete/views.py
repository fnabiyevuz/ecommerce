from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import get_session_key
from apps.cart.api_endpoints.cartitem.CartItemDelete.serializers import CartItemDeleteSerializer
from apps.cart.models import Cart, CartItem


class CartItemDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CartItemDeleteSerializer
    queryset = CartItem.objects.all()

    """
        Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.get(session_key=get_session_key(request))
        instance = self.get_object()
        if instance.cart == cart:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ['CartItemDeleteAPIView']
