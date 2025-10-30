from django.db import models

class Video(models.Model):
    movie_id = models.CharField(max_length=10, primary_key=True)
    movie_title = models.CharField(max_length=200)
    actor1_name = models.CharField(max_length=100)
    actor2_name = models.CharField(max_length=100, blank=True)
    director_name = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=50)
    release_year = models.CharField(max_length=4)

    def __str__(self):
        return self.movie_title