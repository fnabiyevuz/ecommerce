from django.urls import path

from apps.cart.api_endpoints.cart import CartAPIView
from apps.cart.api_endpoints.cartitem import (CartItemCreateAPIView,
                                              CartItemDeleteAPIView,
                                              CartItemListAPIView,
                                              CartItemUpdateAPIView)

app_name = "cart"

urlpatterns = [
    path("my-cart/", CartAPIView.as_view(), name="cart-detail"),
    path("cartitem/", CartItemCreateAPIView.as_view(), name="cartitem-create"),
    path("cartitem/list/", CartItemListAPIView.as_view(), name="cartitem-list"),
    path("cartitem/<int:pk>/delete/", CartItemDeleteAPIView.as_view(), name="cartitem-delete"),
    path("cartitem/<int:pk>/update/", CartItemUpdateAPIView.as_view(), name="cartitem-update"),
]
