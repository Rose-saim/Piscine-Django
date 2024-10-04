# ex10/models.py

from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)  # Ce champ doit être présent
    diameter = models.FloatField()
    orbital_period = models.IntegerField()
    population = models.BigIntegerField(null=True, blank=True)  # Permettre les valeurs nulles
    rotation_period = models.IntegerField()
    surface_water = models.FloatField()
    terrain = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)  # Utiliser des choix de genre ici si nécessaire
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    characters = models.ManyToManyField(People)

    def __str__(self):
        return self.title
