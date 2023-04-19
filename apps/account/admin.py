from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import Account, UserProfile, YouLikeProduct


@admin.register(Account)
class AccountUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    list_display_links = ("username", "email", "phone_number")
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "phone_number", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "firstname",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "user", "city", "state", "address")
    list_filter = ("city", "state")
    list_display_links = ("user", "city", "state", "address")

    def thumbnail(self, object):
        if object.profile_pic:
            return format_html(
                f'<img src="{object.profile_pic.url}" width="80px" height="80px" style="border-radius: 50px;" />'
            )
        else:
            return format_html(
                '<img src="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png" width="40" style="border-radius: 50px;" />'
            )

    thumbnail.short_description = "Profile Picture"

    def set_defult_city(self, request, queryset):
        queryset.update(city="Tashkent City", state="Tashkent")

    set_defult_city.short_description = "Set default Tashkent city"

    actions = ["set_defult_city"]


@admin.register(YouLikeProduct)
class YouLikeProductAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
    list_filter = ("user", "product")
    list_display_links = ("user", "product")

    def set_defult_user(self, request, queryset):
        queryset.update(user=Account.objects.get(username="admin"))

    set_defult_user.short_description = "Set default admin user"

    actions = ["set_defult_user"]
