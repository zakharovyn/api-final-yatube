from rest_framework import pagination
from rest_framework.response import Response


class FollowPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, follows):
        return Response(follows)


class GroupsPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, groups):
        return Response(groups)
