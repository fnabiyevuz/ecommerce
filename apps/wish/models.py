from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel


class WishList(BaseModel):
    user = models.OneToOneField('account.Account', verbose_name=_("User"), on_delete=models.CASCADE,
                                related_name='user_wishlist', blank=True, null=True)
    session_key = models.CharField(verbose_name=_("Session key"), max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("WishList")
        verbose_name_plural = _("WishLists")


class WishListItem(BaseModel):
    wishlist = models.ForeignKey(WishList, verbose_name=_("WishList"), on_delete=models.CASCADE,
                                 related_name='wishlist_items')
    product = models.ForeignKey('product.Product', verbose_name=_("Product"), on_delete=models.CASCADE,
                                related_name='product_wishlistitem')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("WishListItem")
        verbose_name_plural = _("WishListItems")
        unique_together = ('wishlist', 'product')
