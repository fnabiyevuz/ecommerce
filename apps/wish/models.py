from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel


class WishList(BaseModel):
    user = models.ForeignKey('account.Account', verbose_name=_("User"), on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ForeignKey('product.Product', verbose_name=_("Product"), on_delete=models.CASCADE, related_name='product_wishlist')