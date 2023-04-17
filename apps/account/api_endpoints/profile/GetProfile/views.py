from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.account.api_endpoints.profile.GetProfile.serializers import ProfileSerializer


class GetProfileView(generics.RetrieveAPIView):
    """
    Get profile information. Authentication is required!
    """

    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


__all__ = ["GetProfileView"]
