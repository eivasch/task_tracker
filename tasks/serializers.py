from .models import Task, TaskDescription
from comments.models import Comment

from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            # print(self.parent.parent.initial_data)
            return self.get_queryset().get_or_create(task__name=self.parent.parent.initial_data['name'], **{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            print ("In CreatableSlugRelatedField exception")
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class TaskDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDescription
        fields = ['text']


class TaskSerializer(serializers.ModelSerializer):
    description = CreatableSlugRelatedField(slug_field='text', many=True, queryset=TaskDescription.objects.all(),
                                            required=False)
    comment = CreatableSlugRelatedField(slug_field='text', many=True, queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        description_data = validated_data.pop('description')
        task = Task.objects.create(**validated_data)
        for description in description_data:
            TaskDescription.objects.create(task=task, text=description.text)
        return task


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status', 'performer']


class TasksGetSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)
    performer = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    project = serializers.CharField(required=False)
    author = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ["status", "performer", "name", "project", "author"]
