from django.db import models

from .base import BaseModel

from manager.customer import CustomerManager

from enums.main import CustomerStatusEnum
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Customer(AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=400)
    status = models.CharField(max_length=10, choices=CustomerStatusEnum.choices(
    ), default=CustomerStatusEnum.active.value)
    profile_image = models.OneToOneField(
        "File", on_delete=models.CASCADE, null=True)

    created_at = BaseModel.created_at
    updated_at = BaseModel.updated_at

    objects = CustomerManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "customer"
        indexes = [models.Index(fields=["id"], db_tablespace="pk_customer")]

    def __str__(self):
        return self.email
