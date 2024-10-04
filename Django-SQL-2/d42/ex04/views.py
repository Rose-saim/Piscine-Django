from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
# Vue pour créer la table
def init(request):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                episode_nb INTEGER PRIMARY KEY,
                title VARCHAR(64) UNIQUE NOT NULL,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            )
        """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Vue pour insérer les données
def populate(request):
    try:
        cursor = connection.cursor()
        # Liste des films à insérer
        movies = [
            (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
            (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
            (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
            (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
            (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kutz, Rick McCallum', '1980-05-17'),
            (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
            (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
        ]
        
        for movie in movies:
            cursor.execute("""
                INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (title) DO NOTHING
            """, movie)
        
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Vue pour afficher les données
def display(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ex04_movies")
        movies = cursor.fetchall()

        if not movies:
            return HttpResponse("No data available")

        # Formater les résultats en HTML
        html = "<table border='1'><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for movie in movies:
            html += f"<tr><td>{movie[0]}</td><td>{movie[1]}</td><td>{movie[3]}</td><td>{movie[4]}</td><td>{movie[5]}</td></tr>"
        html += "</table>"
        
        return HttpResponse(html)
    except Exception as e:
        return HttpResponse("No data available")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection

def remove(request):
    if request.method == "POST":
        movie_id = request.POST.get("movie_id")
        if movie_id:
            try:
                cursor = connection.cursor()
                # Supprime le film de la table ex04_movies
                cursor.execute("DELETE FROM ex04_movies WHERE episode_nb = %s", (movie_id,))
                messages.success(request, 'Le film a été supprimé avec succès.')
            except Exception as e:
                messages.error(request, f'Erreur lors de la suppression du film: {str(e)}')

            return redirect('remove')  # Redirige vers la même page après suppression

    # Récupère tous les films pour afficher dans la liste déroulante
    cursor = connection.cursor()
    cursor.execute("SELECT episode_nb, title FROM ex04_movies")
    movies = cursor.fetchall()

    return render(request, 'remove.html', {'movies': movies})
