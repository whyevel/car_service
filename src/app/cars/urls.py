from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CarDetail,
    CarListCreate,
    CarMakeDetail,
    CarMakeListCreate,
    CustomerViewSet,
)

router = DefaultRouter()
router.register(r"customers", CustomerViewSet)

urlpatterns = [
    path("cars/", CarListCreate.as_view(), name="car-list-create"),
    path("cars/<int:pk>/", CarDetail.as_view(), name="car-detail"),
    path("carmakes/", CarMakeListCreate.as_view(), name="carmake-list-create"),
    path("carmakes/<int:pk>/", CarMakeDetail.as_view(), name="carmake-detail"),
    path("", include(router.urls)),
]
