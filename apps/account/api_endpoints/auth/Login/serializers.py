from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.account.models import Account


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        username = obj.get("username")
        tokens = Account.objects.get(username=username).tokens
        return tokens

    class Meta:
        model = Account
        fields = ("username", "tokens", "password")

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({"message": "Username or password is not correct"})
        if not user.is_active:
            raise AuthenticationFailed({"message": "Account disabled"})

        data = {
            "username": user.username,
        }
        return data
