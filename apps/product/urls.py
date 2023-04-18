from django.urls import path

from .api_endpoints import ListProductView, ProductDetailView

urlpatterns = [
    path("list/", ListProductView.as_view(), name="list"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
]
