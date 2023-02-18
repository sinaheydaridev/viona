from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status

from .serializers.command_serializer import AdminLoginSerializer

from apps.models.admin import Admin

from utils.token import generate_admin_token
from utils.query import get_queryset


class AdminAuthCommand:
    @staticmethod
    def login(data):
        admin_login_serializer = AdminLoginSerializer(data=data)
        admin_login_serializer.is_valid(raise_exception=True)

        email = data["email"]
        password = data["password"]

        admin = get_queryset(Admin, Q(email=email)).first()
        if admin is None:
            return Response({"detail": "Invalid email or password."}, status.HTTP_400_BAD_REQUEST)

        password_match = admin.check_password(password)
        if not password_match:
            return Response({"detail": "Invalid email or password."}, status.HTTP_400_BAD_REQUEST)

        token = generate_admin_token(admin.id)

        return Response({"token": token}, status.HTTP_200_OK)
