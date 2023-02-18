from rest_framework import serializers

from apps.models.customer import Customer


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["email", "password"]
        extra_kwargs = {"email": {"validators": None}}


class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["username", "email", "fullname", "password"]
        extra_kwargs = {"username": {"validators": None},
                        "email": {"validators": None}}


class CustomerUpdateProfileImageSerializer(serializers.Serializer):
    file_id = serializers.IntegerField()
