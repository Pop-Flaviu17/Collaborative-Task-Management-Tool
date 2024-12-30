from xmlrpc.server import SimpleXMLRPCServer
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collaborative_project_management_tool.settings')
django.setup()

from tasks.models import Task

# Function to update a task's status
def update_task_status(task_id, new_status):
    try:
        task = Task.objects.get(id=task_id)
        task.status = new_status
        task.save()
        return f"Task '{task.title}' updated to status: {new_status}"
    except Task.DoesNotExist:
        return f"Task with ID {task_id} does not exist."

# Start the XML-RPC server
def start_rpc_server():
    with SimpleXMLRPCServer(("localhost", 8000)) as server:
        print("RPC server running on http://localhost:8000")
        server.register_function(update_task_status, "update_task_status")
        server.serve_forever()

if __name__ == "__main__":
    start_rpc_server()