from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status

from apps.models.product import Product

from .serializers.query_serializer import ProductSerializer

from utils.pagination import paginate
from utils.query import get_object, get_queryset


class CustomerProductQuery:
    @staticmethod
    def get_products(query):
        lookups = None

        page = query.get("page", 1)
        limit = query.get("limit", 10)
        title = query.get("title", None)
        statuses = query.getlist("statuses", None)
        max_price = query.get("max_price", None)
        min_price = query.get("min_price", None)
        min_price = query.get("min_price", None)
        sort_type = query.get("sort_type", None)

        products_serializer = ProductSerializer(many=True)
        products = get_queryset(Product)

        if title:
            lookups = Q(title__icontains=title)
            products = get_queryset(Product, lookups)

        if statuses:
            lookups = Q(status__in=statuses) & lookups
            products = get_queryset(Product, lookups)

        if max_price:
            lookups = Q(price__lte=max_price) & lookups
            products = get_queryset(Product, lookups)

        if min_price:
            lookups = Q(price__gte=min_price) & lookups
            products = get_queryset(Product, lookups)

        if sort_type == "asc":
            products = get_queryset(Product, lookups).order_by("created_at")

        if sort_type == "desc":
            products = get_queryset(Product, lookups).order_by("-created_at")

        return Response(paginate(products, products_serializer, page, limit), status.HTTP_200_OK)

    @staticmethod
    def get_product_by_id(product_id):
        product = get_object(Product, product_id)
        product_data = ProductSerializer(product).data
        return Response(product_data, status.HTTP_200_OK)
