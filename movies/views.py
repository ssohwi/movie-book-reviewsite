from django.shortcuts import render
from . import models


def all_movies(request):
    movies = models.Movie.objects.all()
    return render(request, "all_movies.html", context={"movies": movies})
