from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.account.models import Account
from apps.product.models import Product, Review

from .serializers import ReviewPostSerializer


class ReviewProductView(generics.CreateAPIView):
    serializer_class = ReviewPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data["product"]
        product = Product.objects.get(id=product_id)
        desc = request.data["desc"]
        ip = request.META.get("REMOTE_ADDR")
        rating = request.data["rating"]
        review = Review.objects.create(user=user, product=product, desc=desc, ip=ip, rating=rating)
        serializer = self.get_serializer(review)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def validate(self, data):
        user = data["user"]
        product = data["product"]
        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("You have already reviewed this product")
        return data
