from rest_framework import serializers
from .models import Class, Lesson, Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('title', 'description', 'resource_type')

class LessonSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'resources_count', 'resources')

class ClassSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Class
        fields = ('id', 'title', 'description', 'lessons')
