from rest_framework import generics, status
from rest_framework.response import Response

from apps.account.api_endpoints.auth.Register.serializers import RegisterSerializer
from apps.account.models import Account


class AccountRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        username = serializer.data.get("username")
        tokens = Account.objects.get(username=username).tokens
        user_data["tokens"] = tokens
        return Response({"success": True, "data": user_data}, status=status.HTTP_201_CREATED)
