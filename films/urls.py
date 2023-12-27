from django.urls import path, include

from . views import homepage, film_detail, add_films,add_review

app_name = "films"

urlpatterns = [
    path("", homepage, name="home"),
    path("film/<int:pk>/", film_detail, name="f_detail"),
    path("add_films", add_films, name="add_films"),
    path("add_review", add_review, name="add_review"),
]