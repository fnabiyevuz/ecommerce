from apps.cart.choices import CartStatusType
from apps.cart.models import Cart


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
    else:

        cart, _ = Cart.objects.get_or_create(session_key=get_session_key(request))

    return cart
