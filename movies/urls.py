from django.urls import path, include
from rest_framework import routers
from movies.views import MoviesViewSet

router = routers.DefaultRouter()
router.register('', MoviesViewSet)

urlpatterns = [
    path('', include(router.urls))
]