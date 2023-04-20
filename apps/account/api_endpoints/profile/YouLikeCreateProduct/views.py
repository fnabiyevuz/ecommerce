from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import serializers, status
from apps.account.models import YouLikeProduct
from apps.product.models import Product

from .serializers import YouLikeProductSerializer


class YouLikeProductCreate(APIView):
    model = YouLikeProduct
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs.get("product_id"))
        user = request.user
        if not user.is_authenticated:
            raise serializers.ValidationError("User is not authenticated")
        if YouLikeProduct.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("The record already exists")
        saved = YouLikeProduct.objects.create(user=user, product=product)
        return Response({"id": saved.id}, status=status.HTTP_201_CREATED)