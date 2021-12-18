from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import (
    PostSerializer,
    PostCreateSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostUpvoteView(APIView):
    def patch(self, pk, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.upvote_amount += 1
        post.save()
        return Response(status=status.HTTP_200_OK)