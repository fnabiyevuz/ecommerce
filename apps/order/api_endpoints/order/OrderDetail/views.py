from rest_framework import generics

from apps.order.api_endpoints.order.OrderDetail.serializers import \
    OrderDetailSerializer
from apps.order.models import Order


class OrderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


__all__ = ["OrderDetailAPIView"]
