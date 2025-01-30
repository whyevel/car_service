from django.urls import path, include
from .views import CarListCreate, CarDetail, CarMakeListCreate, CarMakeDetail, CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('cars/', CarListCreate.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
    path('carmakes/', CarMakeListCreate.as_view(), name='carmake-list-create'),
    path('carmakes/<int:pk>/', CarMakeDetail.as_view(), name='carmake-detail'),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
]