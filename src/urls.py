from django.contrib import admin
from django.urls import path, include
from app.cars.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.cars.urls')),  # подключение маршрутов приложения cars
    path('', home_view, name='home'),
]