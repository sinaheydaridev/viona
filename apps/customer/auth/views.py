from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

import permissions.main as permissions

from .command import CustomerAuthCommand
from .query import CustomerAuthQuery

prefix = "auth"

get_profile_url_path = f"{prefix}/profile"
login_url_path = f"{prefix}/login"
register_url_path = f"{prefix}/register"
update_profile_url_path = f"{prefix}/profile-image"


class CustomerAuthView(ViewSet):
    query = CustomerAuthQuery
    command = CustomerAuthCommand

    @action(detail=False,
            methods=["GET"],
            url_path=get_profile_url_path,
            permission_classes=[permissions.IsCustomerAuthenticatedPermission])
    def get_profile(self, request):
        customer = request.customer
        return self.query.get_profile(customer)

    @action(detail=False, methods=["POST"], url_path=login_url_path)
    def login(self, request):
        data = request.data
        return self.command.login(data)

    @action(detail=False, methods=["POST"], url_path=register_url_path)
    def register(self, request):
        data = request.data
        return self.command.register(data)

    @action(detail=False,
            methods=["PATCH"],
            url_path=update_profile_url_path,
            permission_classes=[permissions.IsCustomerAuthenticatedPermission])
    def update_profile(self, request):
        data = request.data
        customer = request.customer
        return self.command.update_profile(customer, data)
