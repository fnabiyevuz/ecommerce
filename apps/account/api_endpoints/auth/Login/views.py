from rest_framework import generics, status
from rest_framework.response import Response

from apps.account.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
