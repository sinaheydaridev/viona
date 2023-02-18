from rest_framework import serializers

from apps.models.customer import Customer
from apps.file.serializers.query_file import FileSerializer


class CustomerSerializer(serializers.ModelSerializer):
    profile_image = FileSerializer()

    class Meta:
        model = Customer
        fields = ["username", "email", "fullname",
                  "profile_image", "status", "created_at", "updated_at"]
