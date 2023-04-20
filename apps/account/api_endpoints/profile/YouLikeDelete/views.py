from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.account.models import YouLikeProduct


class ProductDeleteApiView(APIView):
    permission_classes = (IsAuthenticated,)

    lookup_field = "product_id"

    def delete(self, request, product_id):
        saved = get_object_or_404(YouLikeProduct, product_id=product_id, user=request.user)
        saved.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
