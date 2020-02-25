from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Producer(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=50)


class ProducerPreferences(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="producer_preferences"
    )
    user_preference = models.ManyToManyField(Producer)


class GenrePreferences(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="genre_preferences"
    )
    user_preference = models.ManyToManyField(Genre)


class Film(models.Model):
    title = models.CharField(max_length=100)
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        related_name="films"
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="films"
    )


class Rating(models.Model):
    value = models.IntegerField()
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ratings"
    )

    class Meta:
        unique_together = ['film', 'user']
