from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.account.models import Account, UserProfile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "firstname", "phone_number", "email")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "profile_pic", "city", "state", "address")
