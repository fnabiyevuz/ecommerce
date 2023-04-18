from django.urls import include, path

urlpatterns = [
    path("account/", include("apps.account.urls")),
    path("product/", include("apps.product.urls")),
    path("cart/", include("apps.cart.urls")),
    path("chat/", include("apps.chat.urls")),
    path("order/", include("apps.order.urls")),
    path("wishlist/", include("apps.wish.urls")),
]
