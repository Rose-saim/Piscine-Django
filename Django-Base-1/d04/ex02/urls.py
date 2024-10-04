from django.urls import path
from .views import display_form

urlpatterns = [
    path('', display_form, name='ex02_form'),  # URL racine de ex02
]
