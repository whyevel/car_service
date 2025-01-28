from django.urls import path
from .views import CarListCreate, CarDetail, CarMakeListCreate, CarMakeDetail

urlpatterns = [
    path('cars/', CarListCreate.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
    path('carmakes/', CarMakeListCreate.as_view(), name='carmake-list-create'),
    path('carmakes/<int:pk>/', CarMakeDetail.as_view(), name='carmake-detail'),
]