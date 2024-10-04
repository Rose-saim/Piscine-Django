from django.shortcuts import HttpResponse
from .models import Planet, People

def init(request):
    # Crée les tables si elles n'existent pas déjà
    Planet.objects.all().delete()
    People.objects.all().delete()
    return HttpResponse("Tables created or cleared.")

import csv
import os
from django.conf import settings
from django.db import connection
from django.shortcuts import HttpResponse

def populate(request):
    # Chemin des fichiers CSV
    planets_file = os.path.join(settings.BASE_DIR, 'ex08', 'planets.csv')
    people_file = os.path.join(settings.BASE_DIR, 'ex08', 'people.csv')

    try:
        with open(planets_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            with connection.cursor() as cursor:
                cursor.copy_from(f, 'ex08_planets', sep=',', columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))

        with open(people_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            with connection.cursor() as cursor:
                cursor.copy_from(f, 'ex08_people', sep=',', columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))

        return HttpResponse("OK: Data populated.")
    
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

from django.shortcuts import render

def display(request):
    people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name')
    if not people:
        return HttpResponse("No data available.")
    
    return render(request, 'ex08/display.html', {'people': people})
