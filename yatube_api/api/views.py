"""View для приложения api."""

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthenticatedAuthorOrReadOnly
from posts.models import Post, Group
from api.serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
    FollowSerializer,
)
from api.pagination import (
    FollowPagination,
    GroupsPagination,
)

User = get_user_model()


class IsAuthenticatedAuthorOrReadOnlyMixin:
    """Миксин для получения прав."""

    permission_classes = (IsAuthenticatedAuthorOrReadOnly,)


class PostViewSet(IsAuthenticatedAuthorOrReadOnlyMixin, viewsets.ModelViewSet):
    """ViewSet для Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создание объекта с записью в поле юзер автора."""
        serializer.save(author=self.request.user)


class CommentViewSet(
    IsAuthenticatedAuthorOrReadOnlyMixin,
    viewsets.ModelViewSet
):
    """ViewSet для Comment."""

    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination

    def __get_post_or_404(self):
        """Получение поста если он существует."""
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        """Создание объекта комментариев с записью в поле юзер автора."""
        return self.__get_post_or_404().comments.all()

    def perform_create(self, serializer):
        """Создание объекта с записью в поле юзер автора."""
        serializer.save(
            author=self.request.user,
            post=self.__get_post_or_404()
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupsPagination


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """ViewSet для Follow."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']
    pagination_class = FollowPagination

    def get_queryset(self):
        """Получение набора Follow для автора."""
        return self.request.user.followings.all()

    def perform_create(self, serializer):
        """Создание объекта с записью в поле юзер автора."""
        serializer.save(user=self.request.user)
