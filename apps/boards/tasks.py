from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta
  # Replace with the path to your Task model

@shared_task
def send_due_task_reminders():
    """
    This task checks for tasks due tomorrow and sends email reminders
    to the assigned users.
    """
    tomorrow = datetime.now() + timedelta(days=1)
    tasks_due_tomorrow = Task.objects.filter(due_date__date=tomorrow.date())

    for task in tasks_due_tomorrow:
        send_mail(
            subject=f"Reminder: Task '{task.title}' is due tomorrow!",
            message=f"Hello,\n\nThis is a reminder that your task '{task.title}' is due tomorrow ({task.due_date}).",
            from_email='noreply@yourdomain.com',  # Replace with your email
            recipient_list=[task.assigned_to.email],  # Assumes the Task model has an `assigned_to` field
        )

    return f"Reminders sent for {tasks_due_tomorrow.count()} tasks."
