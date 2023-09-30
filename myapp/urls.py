from django.urls import path, include
from . import views

urlpatterns = [
    path("home1/", views.home1, name="home1"),
    path("home2/", views.home2, name="home2"),
    path("home3/", views.home3, name="home3"),
]