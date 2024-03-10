import django_filters
from .models import Film

class FilmFilter(django_filters.FilterSet):
    avg_rating = django_filters.RangeFilter(field_name="avg_rating")
    
    class Meta:
        model = Film
        fields = {"title":["icontains"], 
                #   "released", 
                  "certificate":["exact"], 
                #   "average_rating": ["lt", "gt"]
                  }

