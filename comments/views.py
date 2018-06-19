# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from serializers import CommentSerializer
from models import Comment


@api_view(['PUT'])
def create_comment(request, *args, **kwargs):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        comment = serializer.create(serializer.validated_data)
        return Response(data={'id': comment.pk}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer._errors)


@api_view(['GET'])
def get_comment_info(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(CommentSerializer(comment).data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment.delete()
    return Response(status=status.HTTP_200_OK)
