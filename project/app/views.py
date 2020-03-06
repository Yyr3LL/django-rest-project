from rest_framework import generics, mixins
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProducerCreateView(generics.CreateAPIView):
    serializer_class = ProducerSerializer
    permission_classes = (IsAdminUser, )


class ProducerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProducerSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Producer.objects.all()


class ProducerListView(generics.ListAPIView):
    serializer_class = ProducerSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Producer.objects.all()


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


class UserPreferencesCreateView(generics.CreateAPIView):
    serializer_class = UserPreferencesSerializer
    permission_classes = (IsAuthenticated, )


class UserPreferencesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPreferencesSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return UserPreferences.objects.filter(user=self.request.user)


class UserPreferencesRetrieveView(generics.ListAPIView):
    serializer_class = UserPreferencesSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return UserPreferences.objects.filter(user=self.request.user)


class FilmCreateView(generics.CreateAPIView):
    serializer_class = FilmSerializer
    permission_classes = (IsAuthenticated, )


class FilmDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FilmSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return Film.objects.all()


class FilmListView(generics.ListAPIView):
    serializer_class = FilmSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Film.objects.all()


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
