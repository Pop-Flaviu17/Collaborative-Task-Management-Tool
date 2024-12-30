import xmlrpc.client

# Connect to the RPC server
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Test updating a task
task_id = 1  # Replace with the ID of an actual task in your database
new_status = "In Progress"

try:
    result = server.update_task_status(task_id, new_status)
    print("Server Response:", result)
except Exception as e:
    print("Error:", e)