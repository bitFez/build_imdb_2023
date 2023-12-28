from django.db import models
from django.conf import settings # Add this line to the the bottom of the imports 

certs = [
    ("U", "U"),
    ("PG", "PG"),
    ("12a", "12a"),
    ("15", "15"),
    ("18", "18"),
]

class Film(models.Model):
    title = models.CharField(max_length=250)
    released = models.DateField(auto_now=False, auto_now_add=False)
    certificate = models.CharField(max_length=3, choices=certs)
    duration = models.DurationField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=250)
    star1 = models.CharField(max_length=250)
    star2 = models.CharField(max_length=250)
    star3 = models.CharField(max_length=250)
    star4 = models.CharField(max_length=250)
    overview = models.TextField(max_length=1000)
    poster = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        return self.ratings.all().aggregate(models.Avg("rating")).get("rating__avg", 0.0)
    
    @property
    def No_votes(self):
        return self.ratings.all().aggregate(models.Count("rating")).get("rating__count", 0.0)

class Rating(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.film} - {self.user}"
