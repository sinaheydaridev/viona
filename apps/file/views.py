from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

import permissions.main as permissions

from .command import UploadCommand


post_url_path = "upload"


class FileView(ViewSet):
    command = UploadCommand

    @action(detail=False,
            methods=["POST"],
            url_path=post_url_path,
            permission_classes=[permissions.IsAuthenticatedPermission])
    def post(self, request):
        data = request.data
        return self.command.upload(data=data)
