from rest_framework import serializers
from .models import Genres, Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user','username', 'genres',)



class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username',)
        

class GenreSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name',)