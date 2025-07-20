from rest_framework import pagination
from rest_framework.response import Response


class CustomCommentsPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response(data)


class CustomFollowPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response(data)


class CustomGroupsPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)
