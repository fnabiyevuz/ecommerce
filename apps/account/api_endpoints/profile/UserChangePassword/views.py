from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.account.api_endpoints.profile.UserChangePassword.serializers import SetNewPasswordSerializer


class SetNewPasswordView(generics.UpdateAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": self.request})
        if serializer.is_valid(raise_exception=True):
            return Response({"success": True, "message": "Successfully changed password"}, status=status.HTTP_200_OK)
        return Response({"success": False, "message": "Credentials is invalid"}, status=status.HTTP_400_BAD_REQUEST)
