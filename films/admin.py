from django.contrib import admin

from . models import Film, Rating

# Register your models here.
admin.site.register(Film)
admin.site.register(Rating)