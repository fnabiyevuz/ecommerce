from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg, Count
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

from .choisen import CONDITION

User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"))

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to="product", blank=True, null=True, verbose_name=_("Image"))
    description = models.TextField(verbose_name=_("Description"))
    quantity = models.IntegerField(verbose_name=_("Quantity"))
    rating = models.FloatField(verbose_name=_("Rate"))
    curency = models.CharField(max_length=255, verbose_name=_("Curency"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    type = models.CharField(max_length=255, verbose_name=_("Type"))
    material = models.CharField(max_length=255, verbose_name=_("Material"))
    design = models.CharField(max_length=255, verbose_name=_("Design"))
    customisation = models.CharField(max_length=255, verbose_name=_("Customisation"))
    protection = models.CharField(max_length=255, verbose_name=_("Protection"))
    warranty = models.CharField(max_length=255, verbose_name=_("Warranty"))
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Supplier"))
    manucaturer = models.CharField(max_length=255, verbose_name=_("Manacuater"))
    brand = models.CharField(max_length=255, verbose_name=_("Brand"))
    condition = models.CharField(max_length=255, choices=CONDITION, verbose_name=_("Condition"), default="new")
    view_count = models.IntegerField(default=0, verbose_name=_("View Count"))

    # @property
    # def average_rating(self):
    #     reviews = self.reviews.filter(status=True).aggregate(Avg("rating"))
    #     return float(reviews["rating__avg"]) if reviews["rating__avg"] else 0
    #
    # @property
    # def get_review_count(self):
    #     reviews = self.reviews.filter(status=True).aggregate(count=Count("rating"))
    #     return reviews["count"]

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product", blank=True, null=True, verbose_name=_("Image"))

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)