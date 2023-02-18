from rest_framework import serializers

from apps.models.file import File


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["file_use"]
