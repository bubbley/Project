from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    due = models.DateTimeField()
    calculated_due = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now)


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    due = models.DateTimeField()
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
