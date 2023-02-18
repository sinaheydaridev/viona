import os
from uuid import uuid4

from django.db import models

from .base import BaseModel


def upload_file(_, filepath):
    base_name = os.path.basename(filepath)
    _, ext = os.path.splitext(base_name)
    new_name = f'{uuid4()}{ext}'
    return new_name


class File(models.Model):
    file_use = models.FileField(upload_to=upload_file)

    product = models.ForeignKey(
        "Product", related_name="image_set", on_delete=models.CASCADE, null=True)

    created_at = BaseModel.created_at
    created_at = BaseModel.updated_at

    def __str__(self):
        return self.file_use.name

    class Meta:
        db_table = "file"
        indexes = [models.Index(fields=["id"], db_tablespace="pk_file")]
