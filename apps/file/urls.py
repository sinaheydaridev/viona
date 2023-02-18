from django.urls import path, include

from apps.file import views

from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(prefix=r'file',
                viewset=views.FileView, basename="file")

urlpatterns = [
    path(route="", view=include(router.urls)),
    # path(prefix, views.ProductView.as_view())
]
