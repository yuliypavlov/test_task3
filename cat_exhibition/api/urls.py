from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CatViewSet, BreedViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
