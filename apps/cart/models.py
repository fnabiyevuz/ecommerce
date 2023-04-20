from django.db import models
from django.db.models import F, Sum
from django.utils.translation import gettext as _

from apps.cart.choices import CartStatusType
from apps.common.models import BaseModel


class Cart(BaseModel):
    user = models.ForeignKey(
        "account.Account",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="user_cart",
        blank=True,
        null=True,
    )
    session_key = models.CharField(verbose_name=_("Session key"), max_length=255, blank=True, null=True, unique=True)
    status = models.CharField(
        verbose_name=_("Cart status"), max_length=10, choices=CartStatusType.choices, default=CartStatusType.NEW
    )

    @property
    def total(self):
        return self.cart_items.all().aggregate(total=Sum(F("price") * F("quantity")))["total"] or 0

    def __str__(self):
        return f"{str(self.id)}-cart {self.user}"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, verbose_name=_("Cart"), on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(
        "product.Product", verbose_name=_("Product"), on_delete=models.CASCADE, related_name="product_items"
    )
    quantity = models.IntegerField(verbose_name=_("Quantity"), default=1)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{str(self.cart.id)}-cart {self.product.name} | {self.quantity} * {self.price}"

    def save(self, *args, **kwargs):
        if self.price == 0:
            if self.product.discount_price:
                self.price = self.product.discount_price
            else:
                self.price = self.product.price
        super(CartItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        unique_together = ("cart", "product")
