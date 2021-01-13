from django.shortcuts import render
from . import models
from people.models import Person
from movies.models import Movie
from books.models import Book


def all_categories(request):
    categories = models.Category.objects.all()
    return render(request, "all_categories.html", context={"categories": categories})


def home(request):
    movies = Movie.objects.all()
    books = Book.objects.all()
    people = Person.objects.all()
    categories = models.Category.objects.all()
    return render(
        request,
        "home.html",
        context={
            "movies": movies,
            "books": books,
            "people": people,
            "categories": categories,
        },
    )


def search(request):
    return render(request, "search.html")
