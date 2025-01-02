from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Define the Board model
class Board(models.Model):
    name = models.CharField(max_length=100)  # Name of the board
    description = models.TextField(blank=True, null=True)  # Description of the board
    created_at = models.DateTimeField(auto_now_add=True)  # Created at timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Updated at timestamp
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')  # Board owner (user)

    def _str_(self):
        return self.name

class Column(models.Model):
    name = models.CharField(max_length=100)  # Name of the column (e.g., "To-Do", "In Progress")
    board = models.ForeignKey(Board, related_name='columns', on_delete=models.CASCADE)  # The board to which the column belongs
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the column was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the column was last updated

    def _str_(self):
        return self.name

# Create your models here.
