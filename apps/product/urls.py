from django.urls import path

from .api_endpoints import ListCategoryView, ListProductView, ProductDetailView, RelatedProductView, ReviewProductView

app_name = "product"

urlpatterns = [
    path("list/", ListProductView.as_view(), name="list"),
    path("category/", ListCategoryView.as_view(), name="category"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("related/<int:product_id>/", RelatedProductView.as_view(), name="related"),
    path("review/", ReviewProductView.as_view(), name="review"),
]
