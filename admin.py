from django.contrib import admin
from .models import Film, Cinema, FilmScreening

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    pass

@admin.register(FilmScreening)
class FilmScreeningAdmin(admin.ModelAdmin):
    pass