import admin_thumbnails
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Company, Product, ProductImage


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created_at"


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "created_at")
        exclude = ("image",)


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ("name", "slug", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created_at"


@admin_thumbnails.thumbnail("image")
class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImage
    extra = 2


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"
    list_editable = ("price",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageModelAdmin]


admin.site.register(Product, ProductModelAdmin)
