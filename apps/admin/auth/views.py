from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

import permissions.main as permissions

from .command import AdminAuthCommand
from .query import AdminAuthQuery

prefix = "auth"

get_profile_url_path = f"{prefix}/profile"
login_url_path = f"{prefix}/login"
register_url_path = f"{prefix}/register"
update_profile_url_path = f"{prefix}/profile-image"


class AdminAuthView(ViewSet):
    query = AdminAuthQuery
    command = AdminAuthCommand

    @action(detail=False,
            methods=["GET"],
            url_path=get_profile_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def get_profile(self, request):
        admin = request.admin
        return self.query.get_profile(admin)

    @action(detail=False, methods=["POST"], url_path=login_url_path)
    def login(self, request):
        data = request.data
        return self.command.login(data)
