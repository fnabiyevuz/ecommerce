from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from apps.account.models import YouLikeProduct

from .serializers import YouLikeProductDeleteSerializer


class ProductDeleteApiView(DestroyAPIView):
    queryset = YouLikeProduct.objects.all()
    serializer_class = YouLikeProductDeleteSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
