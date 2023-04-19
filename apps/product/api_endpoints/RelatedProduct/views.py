from rest_framework import generics

from apps.product.models import Product

from .serialzers import RelatedProductSerializer


class RelatedProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = RelatedProductSerializer

    def get_queryset(self):
        category = self.kwargs.get("category__parent_category   ")
        print(category)
        if category:
            return Product.objects.filter(category__parent_category=category)

        else:
            return Product.objects.none()
