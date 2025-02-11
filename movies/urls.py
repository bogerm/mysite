from django.urls import path, include
from rest_framework import routers
from movies.views import MoviesViewSet, ActionViewSet, ComedyViewSet

router = routers.SimpleRouter()
router.register('all', MoviesViewSet, basename='all_movies_router')
router.register('action', ActionViewSet, basename='action_movies_router')
router.register('comedy', ComedyViewSet, basename='comedy_movies_router')

urlpatterns = [
    path('', include(router.urls))
]