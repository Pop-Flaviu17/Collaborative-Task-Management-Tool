from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, default="Pending")  # Pending, In Progress, Completed
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title