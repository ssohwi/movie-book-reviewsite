from django.shortcuts import render
from . import models


def all_books(request):
    books = models.Book.objects.all()
    return render(request, "all_books.html", context={"books": books})
