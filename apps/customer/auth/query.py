from rest_framework.response import Response
from rest_framework import status

from .serializers.query_Serializer import CustomerSerializer


class CustomerAuthQuery:
    @staticmethod
    def get_profile(customer):
        customer_data = CustomerSerializer(customer).data
        return Response(customer_data, status.HTTP_200_OK)
