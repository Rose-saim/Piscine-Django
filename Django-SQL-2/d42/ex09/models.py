from django.db import models
from django.utils import timezone
from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=100)
    diameter = models.IntegerField(default=10000)  # Ajoutez une valeur par défaut
    orbital_period = models.IntegerField(default=365)  # Ajoutez une valeur par défaut
    population = models.BigIntegerField(null=True, blank=True)
    rotation_period = models.IntegerField(null=True, blank=True)
    surface_water = models.FloatField(null=True, blank=True)
    terrain = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, blank=True)
    gender = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=32, blank=True)
    hair_color = models.CharField(max_length=32, blank=True)
    height = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, to_field='name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
