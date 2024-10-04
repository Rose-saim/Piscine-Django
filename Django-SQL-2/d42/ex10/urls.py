# ex10/urls.py

from django.urls import path
from .views import movie_search

urlpatterns = [
    path('', movie_search, name='movie_search'),
]
