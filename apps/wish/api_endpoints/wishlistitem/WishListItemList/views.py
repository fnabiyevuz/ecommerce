from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import get_session_key
from apps.wish.api_endpoints.wishlistitem.WishListItemList.serializers import WishListItemListSerializer
from apps.wish.models import WishListItem, WishList


class WishListItemListAPIView(generics.ListAPIView):
    serializer_class = WishListItemListSerializer
    queryset = WishListItem.objects.all()

    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            wishlist, _ = WishList.objects.get_or_create(user=request.user)
        else:
            wishlist, _ = WishList.objects.get_or_create(session_key=get_session_key(request))
        queryset = wishlist.wishlist_items.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


__all__ = ['WishListItemListAPIView']
