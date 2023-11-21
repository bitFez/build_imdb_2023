from django.shortcuts import render, get_object_or_404

from . models import Film, Rating
# Create your views here.
def homepage(request):
    films = Film.objects.all()

    context = {"films":films}
    return render(request, "films/homepage.html", context)

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    context = {"film":film}
    return render(request, "films/f_detail.html", context)
