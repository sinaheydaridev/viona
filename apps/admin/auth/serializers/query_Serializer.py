from rest_framework import serializers

from apps.models.admin import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["username", "email", "fullname", "created_at", "updated_at"]
