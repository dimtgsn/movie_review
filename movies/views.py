from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Actor, RatingStar, Rating, Genre, Movie, MovieShots, Reviews


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_list.html", {"movie_list": movies})


class MovieDetailView(View):
    """Полное описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})