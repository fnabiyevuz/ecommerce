from rest_framework import generics

from apps.order.api_endpoints.order.OrderUpdate.serializers import \
    OrderUpdateSerializer
from apps.order.models import Order


class OrderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()


__all__ = ["OrderUpdateAPIView"]
