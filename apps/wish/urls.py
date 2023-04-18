from django.urls import path
from apps.wish.api_endpoints.wishlistitem import WishListItemCreateAPIView, WishListItemListAPIView, \
    WishListItemDeleteAPIView

urlpatterns = [
    path("", WishListItemCreateAPIView.as_view(), name='wishlistitem-create'),
    path("list/", WishListItemListAPIView.as_view(), name='wishlistitem-list'),
    path("<int:pk>/delete/", WishListItemDeleteAPIView.as_view(), name='wishlistitem-delete'),
]
