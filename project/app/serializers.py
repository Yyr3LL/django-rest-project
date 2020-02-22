from rest_framework import serializers
from .models import *


class ProducerDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Producer
        fields = "__all__"


class GenreDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Genre
        fields = "__all__"


class FilmDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Film
        fields = "__all__"


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"


class RatingDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = "__all__"


class RatingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
