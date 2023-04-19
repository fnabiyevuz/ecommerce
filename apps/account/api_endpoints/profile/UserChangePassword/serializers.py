from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from apps.account.models import Account


class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=64, write_only=True)

    class Meta:
        model = Account
        fields = ("id", "password", "password2")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        request = self.context["request"]
        user = request.user
        current_password = user.password
        if password != password2:
            raise serializers.ValidationError(
                {"success": False, "message": "Password did not match, " "please try again new"}
            )

        if check_password(password, current_password):
            raise serializers.ValidationError(
                {"success": False, "message": "New password should not similar to current password"}
            )

        user.set_password(password)
        user.save()
        return attrs
