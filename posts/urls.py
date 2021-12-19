from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import CommentViewSet
from posts.views import PostViewSet, PostUpvoteView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
urlpatterns = router.urls

urlpatterns += [
    path('posts/<int:pk>/upvote/', PostUpvoteView.as_view(), name='post-upvote'),
]
