from django.contrib import admin
from .models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    list_display_links = ('id', 'user')
    date_hierarchy = 'created_at'
