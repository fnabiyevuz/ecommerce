from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.account.api_endpoints.profile.YouLikeCreateProduct.serializers import YouLikeProductSerializer
from apps.account.models import Account, YouLikeProduct
from apps.product.models import Product

from .serializers import YouLikeProductGetSerializer


class YouLikeProductGet(generics.ListAPIView):
    model = YouLikeProduct
    serializer_class = YouLikeProductGetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return YouLikeProduct.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = YouLikeProductGetSerializer(queryset, many=True)
        return Response(serializer.data)
