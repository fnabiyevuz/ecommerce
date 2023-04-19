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
        queryset = (
            # Product.objects.filter(category=category) all products in the same category
            Product.objects.filter(category=category).exclude(id=product_id)
            # Product.objects.filter(Q(category=category))
        )
        return queryset
    queryset = Product.objects.all()
    serializer_class = RelatedProductSerializer

    def get_queryset(self):
        category = self.kwargs.get("category__parent_category   ")
        print(category)
        if category:
            return Product.objects.filter(category__parent_category=category)

        else:
            return Product.objects.none()
