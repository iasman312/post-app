from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'author',
            'post',
            'created_at',
        )
        read_only_fields = (
            'id',
            'author',
            'created_at',
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'post',
        )

    def create(self, validated_data):
        comment = Comment(**validated_data)
        comment.author = self.context.user
        comment.save()
        return comment





