from django.urls import path

from apps.order.api_endpoints.coupon import CouponDetailAPIView
from apps.order.api_endpoints.order import (OrderCreateAPIView,
                                            OrderDetailAPIView,
                                            OrderListAPIView,
                                            OrderUpdateAPIView)

app_name = "order"
urlpatterns = [
    path("coupon/<str:code>/", CouponDetailAPIView.as_view(), name="coupon-detail"),
    path("create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("list/", OrderListAPIView.as_view(), name="order-list"),
    path("<int:pk>/detail/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("<int:pk>/update/", OrderUpdateAPIView.as_view(), name="order-update"),
]
