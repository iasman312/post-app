from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'link',
            'author',
            'upvote_amount',
        )
        read_only_fields = (
            'id',
            'author',
            'upvote_amount',
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





