from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "category",
        "cover_image",
        "rating",
        "director",
    )

    list_filter = (
        "year",
        "category",
        "rating",
        "director",
    )

    filter_horizontal = ("cast",)