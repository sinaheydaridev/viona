from rest_framework import serializers

from apps.models.file import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "file_use"]
