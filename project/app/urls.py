from django.urls import path, include
from .views import *

urlpatterns = [
    path(
        'genre/create/',
        GenreCreateView.as_view()
    ),
    path(
        'genre/detail/<int:pk>',
        GenreDetailView.as_view()
    ),
    path(
        'genre/list/',
        GenreListView.as_view()
    ),
    # PREFERENCES VIEWS
    path(
        'preferences/create/',
        UserPreferencesCreateView.as_view()
    ),
    path(
        'preferences/detail/<int:pk>/',
        UserPreferencesDetailView.as_view()
    ),
    path(
        'preferences/get/',
        UserPreferencesRetrieveView.as_view()
    ),
    #FILM VIEWS
    path(
        'film/create/',
        MovieCreateView.as_view()
    ),
    path(
        'film/detail/<int:pk>',
        MovieDetailView.as_view()
    ),
    path(
        'film/list/',
        MovieListView.as_view()
    ),
    # RATINGS VIEWS
    path(
        'rating/create/',
        RatingCreateView.as_view()
    ),
    path(
        'rating/detail/<int:pk>/',
        RatingDetailView.as_view()
    ),
    path(
        'rating/list/',
        RatingCreateView.as_view()
    ),
]
