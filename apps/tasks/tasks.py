from celery import shared_task
import rpyc

@shared_task
def update_tasks_via_rpyc(task_ids, new_status):
    """Asynchronous task to update tasks using RPyC."""
    conn = rpyc.connect("localhost", 18861)
    response = conn.root.bulk_update(task_ids, new_status)
    conn.close()
    return response