from rest_framework import serializers

from apps.models.product import Product, ProductProperty


class CreateProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = ["label", "value"]


class CreateProductSerializer(serializers.ModelSerializer):
    property_ids = serializers.ListField(write_only=True)
    file_ids = serializers.ListField(write_only=True)

    class Meta:
        model = Product
        fields = ["title", "description", "price",
                  "discount_percent", "inventory_count", "property_ids", "file_ids"]


class UpdateProductSerializer(CreateProductSerializer):
    pass
