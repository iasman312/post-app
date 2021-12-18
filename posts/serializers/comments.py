from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
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
        post = Post(**validated_data)
        post.author = self.context.user
        post.save()
        return post





