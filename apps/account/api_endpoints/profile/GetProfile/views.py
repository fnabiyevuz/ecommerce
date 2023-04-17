from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.account.api_endpoints.profile.DeleteProfile.permissions import IsOwnUserOrReadOnly
from apps.account.api_endpoints.profile.GetProfile.serializers import ProfileSerializer
from apps.account.models import UserProfile


class GetProfileView(generics.RetrieveAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsOwnUserOrReadOnly)
    lookup_field = "id"

    def get_object(self):
        return UserProfile.objects.filter(user=self.request.user).first()


__all__ = ["GetProfileView"]
