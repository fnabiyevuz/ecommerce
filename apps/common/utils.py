from apps.cart.choices import CartStatusType
from apps.cart.models import Cart
from apps.order.models import Order


def get_session_key(request) -> str:
    """
    Get session_key or create new one
    """
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
    session_key = request.session.session_key
    return session_key


def get_cart(request):
    """
    Get user's cart or create new one
    """
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user, status=CartStatusType.NEW)
        cart.session_key = request.session.session_key
        cart.save()
    else:

        cart, _ = Cart.objects.get_or_create(session_key=get_session_key(request), status=CartStatusType.NEW)

    return cart


def my_order(request):
    """
    Get user's order
    """
    if request.user.is_authenticated:
        orders = Order.objects.filter(cart__user=request.user)
    else:
        orders = Order.objects.filter(cart__session_key=get_session_key(request))
    return orders
