from django.shortcuts import render, get_object_or_404

from . models import Film, Rating
# Create your views here.
def homepage(request):
    films = Film.objects.all()

    context = {"films":films}
    return render(request, "films/homepage.html", context)

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    total_seconds= int(film.duration.total_seconds())
    hours = total_seconds//3600
    minutes = (total_seconds % 3600 )//60
    duration = f"{hours}h {minutes}m"

    context = {"film":film, "dura":duration}
    return render(request, "films/f_detail.html", context)
