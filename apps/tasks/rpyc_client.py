import rpyc

def bulk_update_tasks(task_ids, new_status):
    conn = rpyc.connect("localhost", 18861)  # Connect to RPyC service
    response = conn.root.bulk_update(task_ids, new_status)
    print(response)
    conn.close()

if __name__ == "__main__":
    # Simulate updating tasks with IDs [1, 2, 3] to 'done'
    bulk_update_tasks([1, 2, 3], 'done')