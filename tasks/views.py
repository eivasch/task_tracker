# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer, TasksGetSerializer


@api_view(['PUT'])
def create_task(request, *args, **kwargs):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.create(serializer.validated_data)
        return Response(data={'id': task.pk}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_task_info(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskUpdateSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.update(task, serializer.validated_data)
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer._errors)


@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    for description in task.description.all():
        description.delete()

    task.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_filtered_tasks(request, *args, **kwargs):
    serializer = TasksGetSerializer(data=request.GET)
    if serializer.is_valid():
        tasks = Task.objects.filter(**serializer.validated_data).all()
        response_data = []
        for task in tasks:
            response_data.append(TaskSerializer(task).data)
        return Response(status=status.HTTP_200_OK, data=response_data)

    return Response(status=status.HTTP_400_BAD_REQUEST)
