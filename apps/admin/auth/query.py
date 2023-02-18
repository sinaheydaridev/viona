from rest_framework.response import Response
from rest_framework import status

from .serializers.query_Serializer import AdminSerializer


class AdminAuthQuery:
    @staticmethod
    def get_profile(admin):
        admin_data = AdminSerializer(admin).data
        return Response(admin_data, status.HTTP_200_OK)
