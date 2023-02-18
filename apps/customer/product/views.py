from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from utils.regex import dynamic_param

from .command import CustomerProductCommand
from .query import CustomerProductQuery

prefix = "product"

get_url_path = prefix
get_detail_url_path = rf"{prefix}/{dynamic_param('product_id')}"


class CustomerProductView(ViewSet):
    query = CustomerProductQuery
    command = CustomerProductCommand

    @action(detail=False, methods=["GET"], url_path=get_url_path)
    def get(self, request):  # Product list
        query = request.GET
        return self.query.get_products(query)

    @action(detail=False, methods=["GET"], url_path=get_detail_url_path)
    def get_detail(self, request,  product_id):  # Product Detail
        return self.query.get_product_by_id(product_id)
