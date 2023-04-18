from django.contrib import admin
from .models import WishList, WishListItem


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key')
    list_display_links = ('id', 'user')
    date_hierarchy = 'created_at'


@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'wishlist', 'product')
    list_display_links = ('id', 'wishlist')
    date_hierarchy = 'created_at'
