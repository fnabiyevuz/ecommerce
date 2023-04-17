from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel


class Cart(BaseModel):
    user = models.ForeignKey('account.Account', verbose_name=_("User"), on_delete=models.CASCADE,
                             related_name='user_cart', blank=True, null=True)
    session_key = models.CharField(verbose_name=_("Session key"), max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{str(self.id)}-cart {self.user.username}"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, verbose_name=_("Cart"), on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('product.Product', verbose_name=_("Product"), on_delete=models.CASCADE,
                                related_name='product_items')
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=1)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{str(self.cart.id)}-cart {self.product.name} | {self.quantity} * {self.price}"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
