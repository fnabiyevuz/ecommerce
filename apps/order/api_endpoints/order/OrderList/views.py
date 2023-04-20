from rest_framework import generics
from rest_framework.response import Response

from apps.common.utils import my_order
from apps.order.api_endpoints.order.OrderList.serializers import \
    OrderListSerializer
from apps.order.models import Order


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    """
        List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = my_order(request)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


__all__ = ["OrderListAPIView"]
