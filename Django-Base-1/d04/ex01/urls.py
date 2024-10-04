from django.urls import path
from .views import django_info, display_process, template_engine

urlpatterns = [
    path('django/', django_info, name='django_info'),
    path('affichage/', display_process, name='display_process'),
    path('templates/', template_engine, name='template_engine'),
]
