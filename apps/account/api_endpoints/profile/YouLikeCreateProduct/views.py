from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.account.models import YouLikeProduct
from apps.product.models import Product

from .serializers import YouLikeProductSerializer


class YouLikeProductCreate(generics.CreateAPIView):
    model = YouLikeProduct
    serializer_class = YouLikeProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        print(request)
        product_id = request.data["product"]
        product = Product.objects.get(id=product_id)
        YouLikeProduct.objects.create(user=user, product=product)
        return Response({"message": "Product added to your like list"}, status=status.HTTP_201_CREATED)
