from celery import shared_task

@shared_task
def send_notification(email):
    print(f"Sending notification to {email}")
    # Simulated email sending logic
    return f"Notification sent to {email}"
