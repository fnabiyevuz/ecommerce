from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from apps.cart.api_endpoints.cartitem.CartItemUpdate.serializers import \
    CartItemUpdateSerializer
from apps.cart.models import CartItem
from apps.common.utils import get_cart


class CartItemUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CartItemUpdateSerializer
    queryset = CartItem.objects.all()

    """
        Update a model instance.
    """

    @swagger_auto_schema(request_body=CartItemUpdateSerializer)
    def update(self, request, *args, **kwargs):
        cart = get_cart(request)
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        if instance.cart == cart:
            if instance.product.quantity + instance.quantity >= request.data['quantity']:
                instance.product.quantity = instance.product.quantity + instance.quantity - request.data['quantity']
                instance.product.save()
            else:
                request.data['quantity'] = instance.product.quantity + instance.quantity

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, "_prefetched_objects_cache", None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ["CartItemUpdateAPIView"]
