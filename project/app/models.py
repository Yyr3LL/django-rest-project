from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    genre_preferences = models.ManyToManyField(Genre, null=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(
        Genre,
        related_name="films",
        null=True
    )
    imdb = models.IntegerField()
    tmdb = models.IntegerField()


class Rating(models.Model):
    value = models.IntegerField()
    film = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="ratings",
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ratings",
        null=True
    )

    class Meta:
        unique_together = ['film', 'user']


