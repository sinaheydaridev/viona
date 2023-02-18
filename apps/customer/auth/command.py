from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status

from .serializers.command_serializer import (CustomerLoginSerializer,
                                             CustomerRegisterSerializer,
                                             CustomerUpdateProfileImageSerializer)

from apps.models.customer import Customer
from apps.models.file import File

from utils.token import generate_customer_token
from utils.query import get_queryset, get_object


class CustomerAuthCommand:
    @staticmethod
    def login(data):
        customer_login_serializer = CustomerLoginSerializer(data=data)
        customer_login_serializer.is_valid(raise_exception=True)

        email = data["email"]
        password = data["password"]

        customer = get_queryset(Customer, Q(email=email)).first()
        if customer is None:
            return Response({"detail": "Invalid email or password."}, status.HTTP_400_BAD_REQUEST)

        password_match = customer.check_password(password)
        if not password_match:
            return Response({"detail": "Invalid email or password."}, status.HTTP_400_BAD_REQUEST)

        token = generate_customer_token(customer.id)

        return Response({"token": token}, status.HTTP_200_OK)

    @staticmethod
    def register(data):
        customer_register_serializer = CustomerRegisterSerializer(data=data)
        customer_register_serializer.is_valid(raise_exception=True)

        username = data["username"]
        email = data["email"]
        fullname = data["fullname"]
        password = data["password"]

        customer_exists = get_queryset(Customer, Q(email=email)).exists()
        if customer_exists:
            return Response({"detail": "Email exists."}, status.HTTP_400_BAD_REQUEST)
        customer_exists = get_queryset(Customer, Q(username=username)).exists()
        if customer_exists:
            return Response({"detail": "Username exists."}, status.HTTP_400_BAD_REQUEST)

        Customer.objects.create_customer(
            email, username, fullname, password)

        return Response({"detail": "Customer created successfully."}, status.HTTP_200_OK)

    @staticmethod
    def update_profile(customer, data):
        customer_Update_profile_image_serializer = CustomerUpdateProfileImageSerializer(
            data=data)
        customer_Update_profile_image_serializer.is_valid(raise_exception=True)

        file_id = data["file_id"]
        file = get_object(File, Q(id=file_id))

        customer.profile_image = file
        customer.save()

        return Response({"detail": "Customer profile image updated successfully."}, status.HTTP_200_OK)
