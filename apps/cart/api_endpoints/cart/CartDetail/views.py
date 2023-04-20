from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cart.api_endpoints.cart.CartDetail.serializers import \
    CartDetailSerializer
from apps.cart.models import Cart
from apps.common.utils import get_cart


class CartAPIView(APIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    def get(self, request):
        cart = get_cart(request)
        serializer = CartDetailSerializer(cart)
        return Response(serializer.data)


__all__ = ["CartAPIView"]
