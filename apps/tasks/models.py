from django.db import models
# Define the Task model

class Task(models.Model):
    title = models.CharField(max_length=200)  # Title of the task
    description = models.TextField(blank=True, null=True)  # Task description
    due_date = models.DateTimeField(blank=True, null=True)  # Due date (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Created at timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Updated at timestamp
    board = models.ForeignKey('Board', related_name='tasks', on_delete=models.CASCADE)  # Board the task belongs to
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Task assignee

    # Task statuses (To-Do, In Progress, Done)
    STATUS_CHOICES = [
        ('todo', 'To-Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='todo',  # Default status is 'To-Do'
    )  # Adding task status with a default of "To-Do"

    def _str_(self):
        return self.title

