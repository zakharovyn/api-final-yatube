from rest_framework import permissions


class IsAuthenticatedAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Права на изменение.

    Разрешает изменение/удаление только автору.
    Остальным — только чтение (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, post):
        return (
            request.method in permissions.SAFE_METHODS
            or post.author == request.user
        )
