from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Collaborative_Task_Management_Tool.settings')

app = Celery('Collaborative_Task_Management_Tool')

# Load settings from Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in apps
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-due-task-reminders': {
        'task': 'apps.tasks.send_due_task_reminders',
        'schedule': crontab(hour="9", minute="0"),  # Runs every day at 9:00 AM
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
