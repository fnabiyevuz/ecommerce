import decimal

from rest_framework import generics, status
from rest_framework.response import Response

from apps.cart.choices import CartStatusType
from apps.cart.models import Cart
from apps.order.api_endpoints.order.OrderCreate.serializers import (
    OrderCreateSerializer, OrderCreateWithCartSerializer)
from apps.order.choices import CouponType
from apps.order.models import Coupon, Order


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    """
        Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(session_key=request.data["session_key"], status=CartStatusType.NEW)
        coupon = Coupon.objects.get(id=request.data["coupon"])
        if coupon.is_available:
            if coupon.discount_type == CouponType.PERCENT:
                if cart.total >= coupon.min_amount:
                    request.data["total"] = (cart.total * (1 - coupon.amount_discount / 100)).quantize(
                        decimal.Decimal(".01")
                    )
                else:
                    raise Exception("Sorry, Cart total is less than the minimum amount")
            else:
                if cart.total >= coupon.min_amount:
                    request.data["total"] = cart.total - coupon.amount_discount
                else:
                    raise Exception("Sorry, Cart total is less than the minimum amount")
        else:
            raise Exception("Sorry, Coupon is not available")

        request.data["cart"] = cart.id
        serializer = OrderCreateWithCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart.status = CartStatusType.ORDERED
        cart.save()
        for item in cart.cart_items.all():
            if item.quantity <= item.product.quantity:
                item.product.quantity -= item.quantity
                item.product.save()
            else:
                item.quantity = item.product.quantity
                item.product.quantity = 0
                item.product.save()
                item.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["OrderCreateAPIView"]
