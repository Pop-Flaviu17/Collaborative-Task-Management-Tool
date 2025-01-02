from django.db import models
from django.contrib.auth.models import User

# Define the Task model
class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    assigned_to = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    board = models.ForeignKey(Board, null=True, blank=True, on_delete=models.SET_NULL)  # Fix this line if Board model exists


