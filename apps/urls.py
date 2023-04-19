from django.urls import include, path

urlpatterns = [
    path("account/", include("apps.account.urls", namespace="account")),
    path("product/", include("apps.product.urls", namespace="product")),
    path("cart/", include("apps.cart.urls", namespace="cart")),
    path("chat/", include("apps.chat.urls", namespace="chat")),
    path("order/", include("apps.order.urls", namespace="order")),
    path("wishlist/", include("apps.wish.urls", namespace="wishlist")),
]
