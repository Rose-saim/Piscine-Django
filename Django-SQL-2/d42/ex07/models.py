from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=200)
    opening_crawl = models.TextField()
    episode_nb = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
