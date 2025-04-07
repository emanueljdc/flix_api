from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        # db_table = ''
        managed = True
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name