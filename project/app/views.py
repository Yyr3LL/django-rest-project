from rest_framework import generics, mixins
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser, )


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Genre.objects.all()


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Genre.objects.all()


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Movie.objects.all()


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Movie.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, )


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)


class RatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Rating.objects.all()
