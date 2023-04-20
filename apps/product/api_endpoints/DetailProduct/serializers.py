from rest_framework import serializers

from apps.product.models import Product, ProductImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image")


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField("get_images")

    def get_images(self, obj):
        return [self.context["request"].build_absolute_uri(image.image.url) for image in obj.images.all()]

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "price",
            "images",
            "description",
            "quantity",
            "rating",
            "currency",
            "discount_price",
            "type",
            "material",
            "design",
            "customization",
            "protection",
            "warranty",
            "supplier",
            "manufacturer",
            "brand",
            "company",
            "condition",
            "view_count",
        )
