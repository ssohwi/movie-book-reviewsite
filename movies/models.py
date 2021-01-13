from django.db import models
from core.models import CoreModel


class Movie(CoreModel):

    """ Movie Model """

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField()
    rating = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies"
    )
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person")

    def __str__(self):
        return self.title
