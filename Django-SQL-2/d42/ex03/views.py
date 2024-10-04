# ex03/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def populate(request):
    data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    response = ""
    for episode_nb, title, director, producer, release_date in data:
        try:
            movie = Movies(
                episode_nb=episode_nb,
                title=title,
                director=director,
                producer=producer,
                release_date=release_date
            )
            movie.save()
            response += f"Inserted {title}: OK<br>"
        except Exception as e:
            response += f"Error inserting {title}: {str(e)}<br>"

    return HttpResponse(response)
# ex03/views.py
def display(request):
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available")

    table = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
    for movie in movies:
        table += f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td></tr>"
    table += "</table>"

    return HttpResponse(table)
# ex03/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('populate/', views.populate, name='populate'),
    path('display/', views.display, name='display'),
]
