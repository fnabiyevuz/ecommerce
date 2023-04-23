from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import filters, generics

from apps.account.api_endpoints.profile.DeleteProfile import permissions
from apps.product.models import Category, Product

from .serializers import CategorySerializer, ProductListSerializer


class ProductFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name="brand")
    price_from = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_to = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    rating_from = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")
    rating_to = django_filters.NumberFilter(field_name="rating", lookup_expr="lte")
    features = django_filters.CharFilter(method="filter_features")

    def filter_features(self, queryset, name, value):
        features = value.split(",")
        for feature in features:
            queryset = queryset.filter(
                Q(type__icontains=feature)
                | Q(material__icontains=feature)
                | Q(design__icontains=feature)
                | Q(customization__icontains=feature)
                | Q(protection__icontains=feature)
                | Q(warranty__icontains=feature)
                | Q(manufacturer__icontains=feature)
            )
        return queryset

    class Meta:
        model = Product
        fields = ["brand", "price_from", "price_to", "rating_from", "rating_to", "features"]


class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ["name", "description", "manufacturer", "brand"]
    ordering_fields = ["name", "price", "rating"]


class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ["name"]







