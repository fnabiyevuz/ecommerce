from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.account.api_endpoints.profile.DeleteProfile.permissions import IsOwnUserOrReadOnly
from apps.product.models import Product

from .serializers import ProductDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (IsAuthenticated, IsOwnUserOrReadOnly)

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        return Response(self.get_serializer(product).data)
