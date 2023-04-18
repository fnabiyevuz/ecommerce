from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import get_session_key
from apps.wish.api_endpoints.wishlistitem.WishListItemCreate.serializers import WishListItemCreateSerializer
from apps.wish.models import WishListItem, WishList


class WishListItemCreateAPIView(generics.CreateAPIView):
    serializer_class = WishListItemCreateSerializer
    queryset = WishListItem.objects.all()

    """
    Create a wishlistitem with authenticated user or session_key.
    """

    def create(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            wishlist, _ = WishList.objects.get_or_create(user=request.user)
        else:
            wishlist, _ = WishList.objects.get_or_create(session_key=get_session_key(request))
        request.data['wishlist'] = wishlist.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ['WishListItemCreateAPIView']
