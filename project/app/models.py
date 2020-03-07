from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=50)


class UserPreferences(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="producer_preferences"
    )
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
        User,
        on_delete=models.CASCADE,
        related_name="ratings",
        null=True
    )

    class Meta:
        unique_together = ['film', 'user']
