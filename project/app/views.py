from rest_framework import generics
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProducerCreateView(generics.CreateAPIView):
    serializer_class = ProducerDetailSerializer
    permission_classes = (IsAdminUser, )


class ProducerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProducerDetailSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Producer.objects.all()


class ProducerListView(generics.ListAPIView):
    serializer_class = ProducerDetailSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Producer.objects.all()


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreDetailSerializer
    permission_classes = (IsAdminUser, )


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreDetailSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Genre.objects.all()


class GenreListView(generics.ListAPIView):
    serializer_class = GenreDetailSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Genre.objects.all()


class FilmCreateView(generics.CreateAPIView):
    serializer_class = FilmDetailSerializer
    permission_classes = (IsAuthenticated, )


class FilmDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FilmDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return Film.objects.all()


class FilmListView(generics.ListAPIView):
    serializer_class = Film
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Film.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)

    def get_queryset(self):
        return Rating.objects.all()


class RatingListView(generics.ListAPIView):
    serializer_class = RatingDetailSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Rating.objects.all()
