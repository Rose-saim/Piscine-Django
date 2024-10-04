from django.urls import path
from .views import markdown_cheatsheet

urlpatterns = [
    path('', markdown_cheatsheet, name='markdown_cheatsheet'),
]
