from django.urls import path, include

from apps.customer.product import views

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(prefix=r'customer',
                viewset=views.CustomerProductView, basename="customer")

urlpatterns = [
    path(route="", view=include(router.urls)),
    # path(prefix, views.ProductView.as_view())
]
