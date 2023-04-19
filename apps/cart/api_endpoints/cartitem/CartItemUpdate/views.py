from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import get_session_key
from apps.cart.api_endpoints.cartitem.CartItemUpdate.serializers import CartItemUpdateSerializer
from apps.cart.models import Cart, CartItem


class CartItemUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CartItemUpdateSerializer
    queryset = CartItem.objects.all()

    """
        Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.get(session_key=get_session_key(request))
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.cart == cart:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ['CartItemUpdateAPIView']
