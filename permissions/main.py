from rest_framework.permissions import BasePermission


class IsAuthenticatedPermission(BasePermission):
    def has_permission(self, request, _):
        admin = request.admin
        customer = request.customer
        if admin or customer:
            return True
        return False


class IsCustomerAuthenticatedPermission(BasePermission):
    def has_permission(self, request, _):
        customer = request.customer
        if customer:
            return True
        return False


class IsAdminAuthenticatedPermission(BasePermission):
    def has_permission(self, request, _):
        admin = request.admin
        if admin:
            return True
        return False
