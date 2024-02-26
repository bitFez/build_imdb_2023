from django.contrib import admin

from . models import Film, Rating

class RatingsAdmin(admin.ModelAdmin):
    list_display = ("film", "user", "rating",)
    list_filter = ("film", "user", "rating",)

# Register your models here.
admin.site.register(Film)
admin.site.register(Rating, RatingsAdmin)