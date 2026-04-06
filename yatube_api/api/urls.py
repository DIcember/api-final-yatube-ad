from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

# Комментарии - вложенный роутинг
posts_router = DefaultRouter()
posts_router.register(
    r'posts/(?P<post_id>\d+)/comments', 
    CommentViewSet, 
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]
