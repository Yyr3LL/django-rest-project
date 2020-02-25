from rest_framework import serializers
from .models import *


class ProducerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ("name", "user")


class ProducerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ProducerPreferencesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProducerPreferences
        fields = "__all__"


class GenrePreferencesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GenrePreferences
        fields = "__all__"


class FilmSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Film
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = "__all__"
