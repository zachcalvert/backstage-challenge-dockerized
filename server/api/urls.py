from django.urls import include, path

from api import views

urlpatterns = [
    path("difference", views.difference, name="difference"),
    path("pythagorean_triplet", views.pythagorean_triplet, name="pythagorean_triplet")
]
