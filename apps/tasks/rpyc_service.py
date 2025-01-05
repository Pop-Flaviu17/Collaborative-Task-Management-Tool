import rpyc
from apps.tasks.models import Task
from django.utils.timezone import now

class TaskService(rpyc.Service):
    def exposed_bulk_update(self, task_ids, status):
        """Update the status of tasks in bulk."""
        Task.objects.filter(id__in=task_ids).update(status=status, updated_at=now())
        return f"Updated {len(task_ids)} tasks to status '{status}'"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(TaskService, port=18861)
    server.start()