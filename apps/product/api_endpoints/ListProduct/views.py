from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from apps.product.models import Product

from .serializers import ProductListSerializer


class ListProductView(generics.ListAPIView):
    """Filter products by name, category, parent category"""

    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("name", "category__name", "category__parent__name")
    permission_classes = [IsAuthenticated]
