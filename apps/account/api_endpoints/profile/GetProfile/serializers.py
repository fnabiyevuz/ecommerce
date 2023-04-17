from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.account.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user", "userfirstname", "profile_pic", "user__phone_number", "user__email")
