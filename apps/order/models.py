import datetime

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from apps.order.choices import CouponType, OrderStatusType, PaymentType


def date_plus_30():
    today = datetime.datetime.now()
    exp_date = today + datetime.timedelta(days=30)
    return exp_date


class Coupon(BaseModel):
    code = models.CharField(verbose_name=_("Code"), max_length=9, null=True, blank=True)
    discount_type = models.CharField(
        verbose_name=_("Discount type"), max_length=25, choices=CouponType.choices, default=CouponType.PERCENT
    )
    amount_discount = models.DecimalField(verbose_name=_("Amount discount"), default=0, decimal_places=2, max_digits=10)
    min_amount = models.DecimalField(verbose_name=_("Minimal amount"), max_digits=12, decimal_places=2, default=0)
    is_available = models.BooleanField(verbose_name=_("Is available?"), default=True)
    expired_date = models.DateTimeField(verbose_name=_("Expired date"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.code is None:
            self.code = get_random_string(length=9, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        if self.expired_date is None:
            self.expired_date = date_plus_30()
        super(Coupon, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"


class Order(BaseModel):
    cart = models.ForeignKey("cart.Cart", verbose_name=_("Cart"), on_delete=models.CASCADE, related_name="cart_orders")
    coupon = models.ForeignKey(Coupon, verbose_name=_("Coupon"), on_delete=models.CASCADE, related_name="coupon_orders")
    total = models.DecimalField(verbose_name=_("Total"), max_digits=12, decimal_places=2)
    order_id = models.CharField(verbose_name=_("Order id"), max_length=11, null=True, blank=True)
    full_name = models.CharField(verbose_name=_("Full name"), max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone number"), region="UZ")
    region = models.ForeignKey(
        "common.Region", verbose_name=_("Region"), on_delete=models.CASCADE, related_name="order_region"
    )
    district = models.ForeignKey(
        "common.District", verbose_name=_("District"), on_delete=models.CASCADE, related_name="order_district"
    )
    note = models.TextField(verbose_name=_("Note"), null=True, blank=True)
    status = models.CharField(
        verbose_name=_("Order status"), max_length=10, choices=OrderStatusType.choices, default=OrderStatusType.NEW
    )
    payment_type = models.CharField(
        verbose_name=_("Payment type"), max_length=10, choices=PaymentType.choices, default=PaymentType.CASH
    )

    def save(self, *args, **kwargs):
        if self.order_id is None:
            self.order_id = get_random_string(length=11, allowed_chars="0123456789")

        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        unique_together = ("cart", "coupon")
