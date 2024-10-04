# ex10/views.py

from django.shortcuts import render
from .models import Movies, People, Planets
from django.db.models import Q

def movie_search(request):
    if request.method == 'POST':
        min_release_date = request.POST.get('min_release_date')
        max_release_date = request.POST.get('max_release_date')
        min_diameter = request.POST.get('min_diameter')
        character_gender = request.POST.get('gender')

        results = People.objects.filter(
            gender=character_gender,
            homeworld__diameter__gte=min_diameter,
            movies__release_date__range=(min_release_date, max_release_date)
        ).distinct()

        if results.exists():
            return render(request, 'ex10/results.html', {'results': results})
        else:
            return render(request, 'ex10/results.html', {'message': 'Nothing corresponding to your research'})

    genders = People.objects.values_list('gender', flat=True).distinct()
    return render(request, 'ex10/search.html', {'genders': genders})
