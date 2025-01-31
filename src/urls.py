from app.cars.views import home
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.cars.urls")),
    path("", home, name="home"),
]
