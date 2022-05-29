from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Actor, RatingStar, Rating, Genre, Movie, MovieShots, Reviews


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})

