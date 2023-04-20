from django.db.models import Q
from rest_framework import generics

from apps.product.models import Product

from .serialzers import RelatedProductSerializer


class RelatedProductView(generics.ListAPIView):
    serializer_class = RelatedProductSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        product = Product.objects.get(id=product_id)
        category = product.category
        queryset = Product.objects.filter(category=category).exclude(id=product_id)
        return queryset
