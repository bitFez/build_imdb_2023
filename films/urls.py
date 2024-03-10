from django.urls import path, include

from . views import homepage, film_detail, add_films, add_reviews, top250,bot250, most_votes, film_qs

app_name = "films"

urlpatterns = [
    path("", homepage, name="home"),
    path("search/", film_qs, name="film_search"),
    path("film/<int:pk>/", film_detail, name="f_detail"),
    path("add_films", add_films, name="add_films"),
    path("add_reviews", add_reviews, name="add_reviews"),
    path("top250", top250, name="top250"),
    path("bot250", bot250, name="bot250"),
    path("most_votes", most_votes, name="most_votes"),
]