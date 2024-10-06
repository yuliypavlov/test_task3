from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Cat, Breed, Rating
from api.serializers import CatSerializer, BreedSerializer, RatingSerializer
from api.permissions import IsOwnerOrReadOnly


class CatViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Cat model.
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Create method that assigns the logged-in user as the owner.
        """
        serializer.save(owner=self.request.user)


class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Breed model.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class RatingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Rating model.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
