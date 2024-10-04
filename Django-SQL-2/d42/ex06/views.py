from django.shortcuts import render
from .models import Ex06Movies
from django.db import connection

# Vue pour initialiser la table
def init(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ex06_movies (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                episode_nb INTEGER,
                opening_crawl TEXT,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        cursor.execute('''
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = NOW();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ LANGUAGE 'plpgsql';
        ''')

        cursor.execute('''
            CREATE TRIGGER update_films_changetimestamp
            BEFORE UPDATE ON ex06_movies
            FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column();
        ''')
    return render(request, 'init.html', {'message': 'Table ex06_movies created successfully.'})

# Vue pour peupler la table
def populate(request):
    # Ajoutez ici vos données à insérer, par exemple
    movies_data = [
        {"title": "The Phantom Menace", "episode_nb": 1, "opening_crawl": "A long time ago in a galaxy far, far away..."},
        # Ajoutez les autres films...
    ]
    
    messages = []
    
    for data in movies_data:
        try:
            movie = Ex06Movies(**data)
            movie.save()
            messages.append(f"Inserted {data['title']}: OK")
        except Exception as e:
            messages.append(f"Error inserting {data['title']}: {str(e)}")
    
    return render(request, 'populate.html', {'messages': messages})

# Vue pour afficher les films
def display(request):
    try:
        movies = Ex06Movies.objects.all()
        if not movies:
            return render(request, 'display.html', {'error': 'No data available.'})
        return render(request, 'display.html', {'movies': movies})
    except Exception as e:
        return render(request, 'display.html', {'error': f'Error: {str(e)}'})

# Vue pour mettre à jour le film
def update(request):
    try:
        movies = Ex06Movies.objects.all()
        if request.method == "POST":
            title = request.POST.get("title")
            opening_crawl = request.POST.get("opening_crawl")
            if title and opening_crawl:
                movie = Ex06Movies.objects.get(title=title)
                movie.opening_crawl = opening_crawl
                movie.save()
                success_message = f'Updated {title}: OK'
                return render(request, 'update.html', {'success': success_message, 'movies': movies})

        if not movies:
            return render(request, 'update.html', {'error': 'No data available.'})

        return render(request, 'update.html', {'movies': movies})
    except Exception as e:
        return render(request, 'update.html', {'error': f'Error: {str(e)}', 'movies': movies})
