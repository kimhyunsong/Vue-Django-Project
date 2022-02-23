from django.http import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from .serializers import GenreSeiralizer, MovieSerializer, ReviewSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Genres, Movie, Review
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model


@api_view(['GET'])
@permission_classes([AllowAny])
def movie(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = []
    genreQ = movie.genres.all()
    for genre in genreQ:
        genres.append({'name': genre.name, 'id': genre.id})
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response({'movies':serializer.data, 'genres':genres})
    else:

        # 분기하여 운영자만 추가 삭제 가능하도록 운영할것.
        serializers = ReviewSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(movie=movie, user=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def movie_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.movie_review.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@api_view(['DELETE'])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET','POST'])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.movie_like_user.filter(pk=request.user.pk).exists():
            return Response({'data': True, 'count':movie.movie_like_user.count()})
        else:
            return Response({'data': False, 'count':movie.movie_like_user.count()})
    
    else:
        if movie.movie_like_user.filter(pk=request.user.pk).exists():
            movie.movie_like_user.remove(request.user)
            return Response({'like': False }, status=status.HTTP_200_OK )
        else:
            movie.movie_like_user.add(request.user)
            return Response({'like': True }, status=status.HTTP_200_OK )




@api_view(['GET', 'POST'])
def movie_watched(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.movie_watched_user.filter(pk=request.user.pk).exists():
            return Response({'watched': True, 'count': movie.movie_watched_user.count()})
        else:
            return Response({'watched': False, 'count': movie.movie_watched_user.count()})

    else:
        if movie.movie_watched_user.filter(pk=request.user.pk).exists():
            movie.movie_watched_user.remove(request.user)
            return Response({'watched': False }, status=status.HTTP_200_OK )
        else:
            movie.movie_watched_user.add(request.user)
            return Response({'watched': True }, status=status.HTTP_200_OK )



@api_view(['GET'])
def movie_search(request, movieName):
    movies = Movie.objects.filter(title__contains=movieName)
    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)




@api_view(['GET'])
def movie_recommend_logined(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    genres = []
    for movie in user.like_movie.all():
        genreQ = movie.genres.all()
        for genre in genreQ:
            genres.append({'name': genre.name, 'id': genre.id})
    genre_list = [0]*20
    genre_dict = {12:1, 14: 2, 16: 3, 18: 4, 27: 5, 28:6, 35:7, 36:8, 37:9, 53:10, 80:11, 90:12, 99:13, 878:14, 9648:15, 10402:16, 10770:17, 10749:18, 10752:19}
    #좋아요가 가장 많은 장르의 영화
    get_genre =0
    for genre in genres:    
        if genre['id'] in genre_dict:
            genre_list[genre_dict.get(genre['id'])] += 1
    for genre, val in genre_dict.items():
        if val == max(genre_list) - 1:
            get_genre = genre
    like_movies = Movie.objects.filter(genres=get_genre)
    genres = []
    for movie in user.watched.all():
        genreQ = movie.genres.all()
        for genre in genreQ:
            genres.append({'name': genre.name, 'id': genre.id})
    genre_list = [0] * 20
    # 시청한 영화중 가장 많은 장르의 영화
    get_genre = 0
    for genre in genres:    
        if genre['id'] in genre_dict:
            genre_list[genre_dict.get(genre['id'])] += 1
    for genre, val in genre_dict.items():
        if val == max(genre_list) - 1:
            get_genre = genre
    watched_movies = Movie.objects.filter(genres=get_genre)
    context = {
        'like_movies': MovieSerializer(like_movies, many=True).data,
        'watched_movies': MovieSerializer(watched_movies, many=True).data
    }
    return Response(context)

            
            
    
  