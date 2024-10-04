from django.db import models

from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=128)
    diameter = models.IntegerField(null=False)
    orbital_period = models.IntegerField(null=False)
    population = models.BigIntegerField(default=0)  # Utilisez un nombre par défaut
    rotation_period = models.IntegerField(null=False)
    surface_water = models.FloatField(default=0.0)  # Utilisez un nombre par défaut
    terrain = models.CharField(max_length=128)
    class Meta:
        db_table = 'ex08_planets'


class People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, blank=True)
    gender = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=32, blank=True)
    hair_color = models.CharField(max_length=32, blank=True)
    height = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    homeworld = models.ForeignKey(Planet, to_field='name', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ex08_people'
