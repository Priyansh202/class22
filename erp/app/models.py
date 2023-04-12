from django.db import models

# Create your models here.

class Class(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resources_count = models.IntegerField()
    classes = models.ManyToManyField(Class, related_name='lessons')

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resource_type = models.CharField(max_length=50)
    lessons = models.ManyToManyField(Lesson, related_name='resources')
