from django.urls import path, include

prefix = "api/"

urlpatterns = [
    path(prefix, include("apps.file.urls")),
    path(prefix, include("apps.admin.auth.urls")),
    path(prefix, include("apps.admin.product.urls")),
    path(prefix, include("apps.customer.auth.urls")),
    path(prefix, include("apps.customer.product.urls")),
]
