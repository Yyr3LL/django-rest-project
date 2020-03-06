from django.urls import path, include
from .views import *

urlpatterns = [
    # PRODUCER VIEWS
    path(
        'producer/create/',
        ProducerCreateView.as_view()
    ),
    path(
        'producer/detail/<int:pk>',
        ProducerDetailView.as_view()
    ),
    path(
        'producer/list/',
        ProducerListView.as_view()
    ),
    # GENRES VIEWS
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
    #"""FILM VIEWS"""
    path(
        'film/create/',
        FilmCreateView.as_view()
    ),
    path(
        'film/detail/<int:pk>',
        FilmDetailView.as_view()
    ),
    path(
        'film/list/',
        FilmListView.as_view()
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
