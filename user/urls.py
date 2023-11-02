from django.urls import path
from .import views


urlpatterns = [
    path("index/", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("menu/", views.menu, name="menu")
]