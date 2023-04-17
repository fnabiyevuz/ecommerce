from rest_framework import serializers

from apps.account.models import UserProfile


class DeleteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("user",)

    def validate(self, attrs):
        user = attrs.get("user")
        if user.is_superuser:
            raise serializers.ValidationError("You cannot delete superuser")
        return attrs
