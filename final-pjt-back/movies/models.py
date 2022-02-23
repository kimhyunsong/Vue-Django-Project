from django.db import models
from django.conf import settings
# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100, null=True, blank=True)
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    popularity = models.IntegerField()
    genres = models.ManyToManyField(Genres, related_name='genres_movie')
    
    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_review")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_review")
    vote = models.FloatField()
