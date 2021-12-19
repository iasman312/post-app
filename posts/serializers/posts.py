from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post
from posts.serializers.comments import CommentSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
        )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'link',
            'author',
            'upvote_amount',
            'comments',
            'created_at',
        )
        read_only_fields = (
            'id',
            'author',
            'upvote_amount',
            'comments',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'link',
        )

    def create(self, validated_data):
        post = Post(**validated_data)
        post.author = self.context.user
        post.save()
        return post
