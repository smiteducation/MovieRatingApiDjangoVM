from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import MoviesViewset, RatingsViewset, UserViewset

router = routers.DefaultRouter()
router.register('users',UserViewset)
router.register('movies',MoviesViewset)
router.register('ratings',RatingsViewset)

urlpatterns = [
    path('', include(router.urls)),
]