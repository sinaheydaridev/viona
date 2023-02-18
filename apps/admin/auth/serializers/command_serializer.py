from rest_framework import serializers

from apps.models.admin import Admin


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["email", "password"]
        extra_kwargs = {"email": {"validators": None}}
