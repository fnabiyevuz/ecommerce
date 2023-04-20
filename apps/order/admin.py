from django.contrib import admin

from .models import Coupon, Order


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "discount_type", "amount_discount", "min_amount", "is_available", "expired_date")
    list_display_links = ("id", "code")
    date_hierarchy = "created_at"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "coupon", "total", "order_id", "full_name", "phone", "status")
    list_display_links = ("id", "cart")
    list_filter = ("region", "district", "status")
    date_hierarchy = "created_at"
