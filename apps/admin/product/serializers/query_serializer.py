from rest_framework import serializers

from apps.models.product import Product, ProductProperty

from apps.file.serializers.query_file import FileSerializer


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    properties = ProductPropertySerializer(many=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    @staticmethod
    def get_images(obj):
        return FileSerializer(obj.image_set.all(), many=True).data
