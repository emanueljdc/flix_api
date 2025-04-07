from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre= models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_data = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)


    class Meta:
        # db_table = ''
        managed = True
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title

