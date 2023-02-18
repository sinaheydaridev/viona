from rest_framework.response import Response
from rest_framework import status

from .serializers.command_file import UploadFileSerializer
from .serializers.query_file import FileSerializer

from apps.models.file import File


class UploadCommand:
    @staticmethod
    def upload(data):
        upload_file_serializer = UploadFileSerializer(data=data)
        upload_file_serializer.is_valid(raise_exception=True)

        file_use = data["file_use"]

        file = File.objects.create(file_use=file_use)
        file_data = FileSerializer(file).data

        return Response(file_data, status.HTTP_201_CREATED)
