from django.db import models
from musicians.models import Musician

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_name = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.album_name
