# ex05/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie

# Données à insérer
MOVIE_DATA = [
    (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
    (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
    (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
    (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
    (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'),
    (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
    (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
]

def populate(request):
    messages = []
    for episode_nb, title, director, producer, release_date in MOVIE_DATA:
        movie, created = Movie.objects.update_or_create(
            episode_nb=episode_nb,
            defaults={
                'title': title,
                'director': director,
                'producer': producer,
                'release_date': release_date,
            }
        )
        if created:
            messages.append(f"Inserted: {title} (Episode {episode_nb})")
        else:
            messages.append(f"Updated: {title} (Episode {episode_nb})")

    return HttpResponse("<br>".join(messages) or "No data inserted.")

def display(request):
    try:
        movies = Movie.objects.all()
        if not movies:
            return HttpResponse("No data available")

        html = "<table border='1'><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for movie in movies:
            html += f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td></tr>"
        html += "</table>"
        
        return HttpResponse(html)
    except Exception:
        return HttpResponse("No data available")

from django.shortcuts import render
from .models import Movie


def remove(request):
    try:
        # Récupère tous les films
        movies = Movie.objects.all()
        print(f"Available movies: {[movie.title for movie in movies]}")  # Pour déboguer

        if request.method == "POST":
            # Récupère le numéro d'épisode du film sélectionné
            episode_nb = request.POST.get("1")  # Utilisez episode_nb ici
            print(f"Selected movie episode_nb: {episode_nb}")  # Pour déboguer

            if episode_nb:
                try:
                    # Trouve le film par episode_nb
                    movie = Movie.objects.get(episode_nb=episode_nb)
                    movie.delete()  # Supprime le film
                    success_message = f'Movie "{movie.title}" removed successfully!'
                    # Retourne à la même page avec un message de succès
                    return render(request, 'remove.html', {'success': success_message, 'movies': Movie.objects.all()})
                except Movie.DoesNotExist:
                    error_message = 'Movie not found'
                    return render(request, 'remove.html', {'error': error_message, 'movies': movies})

        # Si on arrive ici, c'est soit une requête GET, soit le POST n'a pas réussi à supprimer un film
        if not movies:
            return render(request, 'remove.html', {'error': 'No movies available', 'movies': movies})

        # Affiche la liste des films
        return render(request, 'remove.html', {'movies': movies})  
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render(request, 'remove.html', {'error': error_message, 'movies': movies})
