from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from utils.regex import dynamic_param

import permissions.main as permissions

from .command import AdminProductCommand
from .query import AdminProductQuery

prefix = "product"

get_url_path = prefix
post_url_path = prefix
get_detail_url_path = rf"{prefix}/{dynamic_param('product_id')}"
update_product_url_path = rf"{prefix}/{dynamic_param('product_id')}"
create_product_property_url_path = rf"{prefix}/property"


class AdminProductView(ViewSet):
    query = AdminProductQuery
    command = AdminProductCommand

    @action(detail=False,
            methods=["GET"],
            url_path=get_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def get(self, request):  # Product list
        query = request.GET
        return self.query.get_products(query)

    @action(detail=False,
            methods=["GET"],
            url_path=get_detail_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def get_detail(self, request,  product_id):  # Product Detail
        return self.query.get_product_by_id(product_id)

    @action(detail=False,
            methods=["POST"],
            url_path=post_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def post(self, request):  # Create Product
        data = request.data
        return self.command.create_product(data=data)

    @action(detail=False,
            methods=["PUT"],
            url_path=post_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def put(self, request, product_id):  # Update Product
        data = request.data
        return self.command.update_product(product_id, data=data)

    @action(detail=False,
            methods=["DELETE"],
            url_path=post_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def delete(self, request, product_id):  # Delete Product
        return self.command.delete_product(product_id)

    @action(detail=False,
            methods=["POST"],
            url_path=create_product_property_url_path,
            permission_classes=[permissions.IsAdminAuthenticatedPermission])
    def create_product_property(self, request):
        data = request.data
        return self.command.create_product_property(data)
