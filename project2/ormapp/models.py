from django.db import models
from django.contrib import admin

class Movie_DB(models.Model):
    Movie_ID = models.CharField(max_length=20, primary_key=True)
    Title = models.CharField(max_length=100)
    Genre = models.CharField(max_length=20)
    Rating = models.IntegerField()
    Language = models.CharField(max_length=15)
    Release_Date = models.DateField()
    Poster = models.ImageField()

class Movie_DBAdmin(admin.ModelAdmin):
    list_display = ('Movie_ID', 'Title', 'Genre', 'Rating',
                    'Language', 'Release_Date', 'Poster')

