from django.shortcuts import render
from .models import People, Planets

def display_characters(request):
    characters = People.objects.filter(homeworld__climate__icontains='windy').select_related('homeworld').order_by('name')

    if not characters:
        return render(request, 'ex09/no_data.html', {
            'message': "No data available, please use the following command line before use:",
            'command': "python manage.py loaddata ex09_initial_data.json"
        })

    return render(request, 'ex09/display.html', {'characters': characters})
