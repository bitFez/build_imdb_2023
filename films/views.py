from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
import os, json
from datetime import timedelta
from django.http import HttpResponse
from django.core.paginator import Paginator
from random import randint
from django.contrib.auth.models import User

from . models import Film, Rating
module_dir = os.path.dirname(__file__)  # get current directory
# Create your views here.
def add_films(request):
    file_path = os.path.join(module_dir, 'imdb_top_films.json')
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    no_added = 0
    for film in data:
        dur = film["Runtime"]
        f_dur = timedelta(minutes=int(dur[0:-4]))
        obj = Film.objects.update_or_create(
            title = film["Series_Title"],
            released = f"{film['Released_Year']}-01-01",
            certificate = film["Certificate"],
            duration = f_dur,
            genre = film["Genre"],
            director = film["Director"],
            star1 = film["Star1"],
            star2 = film["Star2"],
            star3 = film["Star3"],
            star4 = film["Star4"],
            overview = film["Overview"],
            poster = film["Poster_Link"]
        )
        no_added += 1
    msg = f"Added {no_added} films to the database."
    return HttpResponse(msg, content_type="text/plain")

def add_reviews(given_film, given_user, given_rating):
    obj = Rating.objects.update_or_create(
        film = get_object_or_404(Film, pk=given_film),
        user = get_object_or_404(User, pk=given_user),
        rating = given_rating
    )
    

def homepage(request):
    films = Film.objects.all()
    paginator = Paginator(films, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"films":films, "page_obj":page_obj}
    return render(request, "films/homepage.html", context)

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    total_seconds= int(film.duration.total_seconds())
    hours = total_seconds//3600
    minutes = (total_seconds % 3600 )//60
    duration = f"{hours}h {minutes}m"
    genres = film.genre.split(",")
    context = {"film":film, "dura":duration, "genres":genres}
    return render(request, "films/f_detail.html", context)

def add_review(request):
    for i in range(1,5):
        filmID = randint(1,680)
        film_rating = randint(1,10)
        add_reviews(filmID, i, film_rating)
    return redirect("films:home")