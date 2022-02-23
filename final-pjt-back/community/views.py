from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import status
from .models import Post, PostComment
from .serializers import PostSerializer, PostCommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.http import require_POST
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['GET', 'POST'])
def community(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, page):
    post = get_object_or_404(Post, pk=page)
    if request.method =='GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.user == post.user:
        if request.method == 'PUT':
            serializer = PostSerializer(instance=post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method=='DELETE':
            post.delete()
            data={
                'data': f'게시글 {page}번이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    else:
        data={
            'data': '게시글 접근 권한이 없습니다.'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
def comment_list(request, page):
    post = get_object_or_404(Post, pk=page)
    if request.method == 'GET':
        comments = post.post_comments.all()
        serializer = PostCommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET','POST'])
def post_likes(request, page):
    post = get_object_or_404(Post, pk=page)
    if request.method == 'GET':
        likes = post.post_like_user.all().count()
        if post.post_like_user.all().filter(pk=request.user.pk).exists():
            value = True
            return Response({'likes_count':likes, 'value':value })
        else:
            value = False
            return Response({'likes_count':likes, 'value':value})
        
    if request.method=='POST':
        # 유저가 좋아요 버튼을 누름
        # 만약에 유저가 좋아요 버튼을 누른 상태이면
        # == 유저를 가져와 포스트에 좋아요를 누른 유저 아이디를 찾는다
        # 토글
        # 포스트에 
        if post.post_like_user.all().filter(pk=request.user.pk).exists():
            post.post_like_user.remove(request.user)
            return Response({'like':False}, status=status.HTTP_200_OK)
        else:
            post.post_like_user.add(request.user)
            return Response({'like':True}, status=status.HTTP_200_OK)








@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_detail(request, page, comment_pk):
    comment = get_object_or_404(PostComment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'DELETE':
            comment.delete()
            data = {
                'data': f'comment {comment_pk}번이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)



