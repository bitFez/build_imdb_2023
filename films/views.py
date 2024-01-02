from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Avg, Count
import os, json
from datetime import timedelta
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from random import randint

from . models import Film, Rating
module_dir = os.path.dirname(__file__)  # get current directory
# Create your views here.
def top250(request):
    films = Film.objects.annotate(avr=Avg("ratings__rating"), votes=Count("ratings__rating")).order_by("-avr")[0:250]
    paginator = Paginator(films, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"films":films, "page_obj":page_obj}
    return render(request, "films/homepage.html", context)

def most_votes(request):
    films = Film.objects.annotate(avr=Avg("ratings__rating"), votes=Count("ratings__rating")).order_by("-votes")[0:250]
    paginator = Paginator(films, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"films":films, "page_obj":page_obj}
    return render(request, "films/homepage.html", context)

def bot250(request):
    films = Film.objects.annotate(avr=Avg("ratings__rating")).order_by("avr")[0:250]
    paginator = Paginator(films, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"films":films, "page_obj":page_obj}
    return render(request, "films/homepage.html", context)

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
    
def add_rev(g_film, g_user, g_rating):
    obj = Rating.objects.update_or_create(
        film = get_object_or_404(Film, pk=g_film),
        user = get_object_or_404(User, pk=g_user),
        rating = g_rating,
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

def add_reviews(request):
    for j in range(0,10000):
        for i in range(1,5):
            filmID = randint(1,692)
            filmRating = randint(1,10)
            add_rev(filmID, i, filmRating)
    return redirect("films:home")