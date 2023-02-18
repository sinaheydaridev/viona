from django.db import models

from .base import BaseModel

from enums.main import ProductStatusEnum


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    discount_percent = models.IntegerField()
    sales_number = models.IntegerField(default=0)
    inventory_count = models.IntegerField()
    properties = models.ManyToManyField(
        "ProductProperty", related_name="properties", null=True)
    status = models.CharField(max_length=1,
                              choices=ProductStatusEnum.choices(),
                              default=ProductStatusEnum.available.value)
    is_visible = models.BooleanField(default=True)

    created_at = BaseModel.created_at
    updated_at = BaseModel.updated_at

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"
        indexes = [models.Index(fields=["id"], db_tablespace="pk_product")]


class ProductProperty(models.Model):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=400)

    created_at = BaseModel.created_at
    updated_at = BaseModel.updated_at

    def __str__(self):
        return self.label

    class Meta:
        db_table = "product_property"
        indexes = [models.Index(fields=["id"], db_tablespace="pk_property")]
