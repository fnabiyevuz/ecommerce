from django.urls import path

from apps.cart.api_endpoints.cartitem import CartItemCreateAPIView, CartItemListAPIView, CartItemDeleteAPIView, CartItemUpdateAPIView

urlpatterns = [
    path("", CartItemCreateAPIView.as_view(), name="cartitem-create"),
    path("list/", CartItemListAPIView.as_view(), name="cartitem-list"),
    path("<int:pk>/delete/", CartItemDeleteAPIView.as_view(), name='cartitem-delete'),
    path("<int:pk>/update/", CartItemUpdateAPIView.as_view(), name='cartitem-update'),
]
