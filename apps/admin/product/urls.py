from django.urls import path, include

from apps.admin.product import views

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(prefix=r'admin',
                viewset=views.AdminProductView, basename="admin")

urlpatterns = [
    path(route="", view=include(router.urls)),
    # path(prefix, views.ProductView.as_view())
]
