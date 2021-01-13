from django.shortcuts import render
from . import models


def all_people(request):
    people = models.Person.objects.all()
    return render(request, "all_people.html", context={"people": people})
