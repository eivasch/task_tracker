from .models import Comment
from tasks.models import Task

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    task = serializers.SlugRelatedField(slug_field='pk', queryset=Task.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'
