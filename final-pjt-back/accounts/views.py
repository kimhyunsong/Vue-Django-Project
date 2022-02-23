from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from community.models import Post
from community.serializers import PostSerializer
from movies.serializers import MovieSerializer

# Create your views here.



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')
    if password != passwordConfirmation:
        return Response({'비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)


    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    like_movies = list(user.like_movie.all().values())
    watched_movies = list(user.watched.all().values())
    like_posts = list(user.like_post.all().values())
    posts_user = Post.objects.all().filter(user_id=request.user.pk)
    context = {
        'like_movies': like_movies,
        'watched_movies': watched_movies,
        'like_posts': like_posts,
        'posts_user': PostSerializer(posts_user, many=True).data,
    }
    return JsonResponse(context)
    
    
    
            
        
    




@api_view(['PUT', 'DELETE'])
def update(request, username):
    user = request.user
    if request.user.username != username:
        return Response({'data':'잘못된 접근입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        password = request.data.get('password')
        passwordConfirmation = request.data.get('passwordConfirmation')
        if password != passwordConfirmation:
            return Response({'비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'data':'그동안 이용해주셔서 감사합니다.'}, status=status.HTTP_204_NO_CONTENT)
