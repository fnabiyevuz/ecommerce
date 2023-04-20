from rest_framework import generics

from apps.order.api_endpoints.coupon.CouponDetail.serializers import \
    CouponDetailSerializer
from apps.order.models import Coupon


class CouponDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CouponDetailSerializer
    queryset = Coupon.objects.all()
    lookup_field = "code"


__all__ = ["CouponDetailAPIView"]
