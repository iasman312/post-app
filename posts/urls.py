from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
urlpatterns = router.urls

