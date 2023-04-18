from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import get_session_key
from apps.wish.api_endpoints.wishlistitem.WishListItemDelete.serializers import WishListItemDeleteSerializer
from apps.wish.models import WishListItem, WishList


class WishListItemDeleteAPIView(generics.DestroyAPIView):
    serializer_class = WishListItemDeleteSerializer
    queryset = WishListItem.objects.all()

    """
        Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            wishlist = WishList.objects.get(user=request.user)
        else:
            wishlist = WishList.objects.get(session_key=get_session_key(request))
        instance = self.get_object()
        if instance.wishlist == wishlist:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ['WishListItemDeleteAPIView']
