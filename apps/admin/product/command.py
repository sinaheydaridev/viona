from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status

from .serializers.command_serializer import CreateProductSerializer, CreateProductPropertySerializer, UpdateProductSerializer
from .serializers.query_serializer import ProductSerializer, ProductPropertySerializer

from apps.models.product import Product, ProductProperty
from apps.models.file import File

from utils.query import get_object, get_queryset


class AdminProductCommand:
    @staticmethod
    def create_product(data):
        create_product_serializer = CreateProductSerializer(data=data)
        create_product_serializer.is_valid(raise_exception=True)

        title = data["title"]
        description = data["description"]
        price = data["price"]
        discount_percent = data["discount_percent"]
        inventory_count = data["inventory_count"]
        property_ids = data["property_ids"]
        file_ids = data["file_ids"]

        files = get_queryset(File, Q(id__in=file_ids))
        product_properties = get_queryset(ProductProperty,
                                          Q(id__in=property_ids))
        product = Product.objects.create(title=title,
                                         description=description,
                                         price=price,
                                         discount_percent=discount_percent,
                                         inventory_count=inventory_count)
        product.image_set.set(files)
        product.properties.set(product_properties)

        product_data = ProductSerializer(product).data
        return Response(product_data, status.HTTP_201_CREATED)

    @staticmethod
    def update_product(product_id, data):
        update_product_serializer = UpdateProductSerializer(data=data)
        update_product_serializer.is_valid(raise_exception=True)

        title = data["title"]
        description = data["description"]
        price = data["price"]
        discount_percent = data["discount_percent"]
        inventory_count = data["inventory_count"]
        property_ids = data["property_ids"]
        file_ids = data["file_ids"]

        files = get_queryset(File, Q(id__in=file_ids))
        product_properties = get_queryset(ProductProperty,
                                          Q(id__in=property_ids))
        product = get_object(Product, product_id)

        product.title = title
        product.description = description
        product.price = price
        product.discount_percent = discount_percent
        product.inventory_count = inventory_count
        product.image_set.set(files)
        product.properties.set(product_properties)
        product.save()

        product_data = ProductSerializer(product).data
        return Response(product_data, status.HTTP_200_OK)

    @staticmethod
    def delete_product(product_id):
        product = get_object(Product, product_id)
        product.delete()
        return Response(None, status.HTTP_200_OK)

    @staticmethod
    def create_product_property(data):
        create_product_property_serializer = CreateProductPropertySerializer(
            data=data)
        create_product_property_serializer.is_valid(raise_exception=True)

        label = data["label"]
        value = data["value"]

        product_property = ProductProperty.objects.create(
            label=label, value=value)
        product_property_data = ProductPropertySerializer(
            product_property).data

        return Response(product_property_data, status.HTTP_201_CREATED)
