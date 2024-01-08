from django.contrib import admin

from . models import Film, Rating

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('film', 'user', 'rating',)
    list_filter = ('film', 'user', 'rating',)
admin.site.register(Film)
admin.site.register(Rating, RatingAdmin)