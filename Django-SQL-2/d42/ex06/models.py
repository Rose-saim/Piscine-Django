from django.db import models

class Ex06Movies(models.Model):
    title = models.CharField(max_length=255)
    episode_nb = models.IntegerField()
    opening_crawl = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Date de création
    updated = models.DateTimeField(auto_now=True)  # Date de mise à jour

    def __str__(self):
        return self.title
