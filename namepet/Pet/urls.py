from django.urls import path

from . import views

urlpatterns = [
    path("unnamed/", views.list_unnamed, name="list"),
    path("cats/", views.list_cats, name = "list"),
    path("dogs/", views.list_dogs, name = "list")
]