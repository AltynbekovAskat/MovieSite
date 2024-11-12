from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movie', MovieListViewSet, basename='movielist')
router.register(r'users', ProfileViewSet, basename='user_list')
router.register(r'reviews', RatingViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls))
]


