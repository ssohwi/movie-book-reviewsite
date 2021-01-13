from django.urls import path
from books import views as book_views
from categories import views as category_views
from movies import views as movie_views
from people import views as person_views

app_name = "core"

urlpatterns = [
    path("", category_views.home, name="home"),
    path("search/", category_views.search, name="search"),
    path("categories/", category_views.all_categories, name="categories"),
    path("books/", book_views.all_books, name="books"),
    path("movies/", movie_views.all_movies, name="movies"),
    path("people/", person_views.all_people, name="people"),
]
