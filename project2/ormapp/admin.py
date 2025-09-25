from django.contrib import admin
from .models import Movie_DB, Movie_DBAdmin
admin.site.register(Movie_DB, Movie_DBAdmin)