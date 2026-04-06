from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment, Group, Follow
from .serializers import (
    PostSerializer, CommentSerializer, 
    GroupSerializer, FollowSerializer
)
from .permissions import IsAuthorOrReadOnly

class CustomPagination(PageNumberPagination):
    """Кастомная пагинация для возврата списка"""
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # ← Важно: для групп НЕТ пагинации по ТЗ, но должен возвращаться список!

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]  # ← только для авторизованных!
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
