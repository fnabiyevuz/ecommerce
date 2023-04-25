from rest_framework import generics
from rest_framework.response import Response

from apps.common.utils import my_cart
from apps.cart.api_endpoints.cart.CartList.serializers import \
    CartListSerializer
from apps.cart.models import Cart


class CartListAPIView(generics.ListAPIView):
    serializer_class = CartListSerializer
    queryset = Cart.objects.all()

    """
        List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = my_cart(request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


__all__ = ["CartListAPIView"]
