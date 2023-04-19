from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.account.models import Account


class LoginSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=100, required=True)
    phone_number = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        phone_number = obj.get("phone_number")
        tokens = Account.objects.get(phone_number=phone_number).tokens
        return tokens

    class Meta:
        model = Account
        fields = ("phone_number", "tokens", "password")

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        print(phone_number)
        password = attrs.get("password")
        user = authenticate(phone_number=phone_number, password=password)
        print(user)
        if not user:
            raise AuthenticationFailed({"message": "Phone number or password is not correct"})
        if not user.is_active:
            raise AuthenticationFailed({"message": "Account disabled"})

        data = {
            "phone_number": user.phone_number,
        }
        return data
