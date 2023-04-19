from rest_framework import generics
from rest_framework.response import Response

from apps.common.utils import get_session_key
from apps.cart.api_endpoints.cartitem.CartItemList.serializers import CartItemListSerializer
from apps.cart.models import CartItem, Cart


class CartItemListAPIView(generics.ListAPIView):
    serializer_class = CartItemListSerializer
    queryset = CartItem.objects.all()

    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            cart, _ = Cart.objects.get_or_create(session_key=get_session_key(request))
        queryset = cart.cart_items.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


__all__ = ['CartItemListAPIView']
