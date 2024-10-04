from django.shortcuts import render, redirect
from .models import Movies
from django.http import HttpResponse

def populate(request):
    # Insérez vos données ici, comme à l'exercice ex02
    movies_data = [
        {'title': 'The Phantom Menace', 'opening_crawl': 'A long time ago in a galaxy far, far away...', 'episode_nb': 1},
        {'title': 'Attack of the Clones', 'opening_crawl': 'It is a dark time for the Rebellion...', 'episode_nb': 2},
        {'title': 'Revenge of the Sith', 'opening_crawl': 'The saga continues...', 'episode_nb': 3},
        {'title': 'A New Hope', 'opening_crawl': 'In a galaxy far, far away...', 'episode_nb': 4},
        {'title': 'The Empire Strikes Back', 'opening_crawl': 'The dark side of the Force...', 'episode_nb': 5},
        {'title': 'Return of the Jedi', 'opening_crawl': 'Luke Skywalker has returned...', 'episode_nb': 6},
        {'title': 'The Force Awakens', 'opening_crawl': 'The Force awakens...', 'episode_nb': 7},
    ]
    messages = []
    for data in movies_data:
        try:
            movie = Movies(**data)
            movie.save()
            messages.append(f"{data['title']}: OK")
        except Exception as e:
            messages.append(f"{data['title']}: Erreur - {str(e)}")
    return render(request, 'ex07/populate.html', {'messages': messages})

def display(request):
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available.")
    return render(request, 'ex07/display.html', {'movies': movies})

def update(request):
    if request.method == 'POST':
        selected_movie_id = request.POST.get('movie_id')
        new_opening_crawl = request.POST.get('opening_crawl')
        try:
            movie = Movies.objects.get(id=selected_movie_id)
            movie.opening_crawl = new_opening_crawl
            movie.save()
            return redirect('ex07:update')
        except Movies.DoesNotExist:
            return HttpResponse("Movie not found.")
    movies = Movies.objects.all()
    if not movies:
        return HttpResponse("No data available.")
    return render(request, 'ex07/update.html', {'movies': movies})
