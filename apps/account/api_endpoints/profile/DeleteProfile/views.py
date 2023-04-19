from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnUserOrReadOnly
from .serializers import DeleteProfileSerializer


class DeleteProfileView(generics.DestroyAPIView):
    serializer_class = DeleteProfileSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnUserOrReadOnly,
    )

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.delete()
