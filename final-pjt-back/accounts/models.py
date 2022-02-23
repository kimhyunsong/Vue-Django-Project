from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
from community.models import Post

# Create your models here.
class User(AbstractUser):
    like_movie = models.ManyToManyField(Movie, related_name='movie_like_user')
    watched = models.ManyToManyField(Movie, related_name='movie_watched_user')
    like_post = models.ManyToManyField(Post, related_name='post_like_user')
