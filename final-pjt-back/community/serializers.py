from rest_framework import serializers
from .models import Post,PostComment


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user','username',)



class PostCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = PostComment
        fields = '__all__'
        read_only_fields = ('user','username', 'post',)
