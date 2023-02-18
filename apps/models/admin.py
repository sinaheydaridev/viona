from django.db import models

from .base import BaseModel

from manager.admin import AdminManager

from django.contrib.auth.models import AbstractBaseUser


class Admin(AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=400)

    created_at = BaseModel.created_at
    updated_at = BaseModel.updated_at

    objects = AdminManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "admin"
        indexes = [models.Index(fields=["id"], db_tablespace="pk_admin")]

    def __str__(self):
        return self.email
