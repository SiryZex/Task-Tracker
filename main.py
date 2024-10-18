import sys
from tasktracker import TaskTracker

def main():
    task_tracker = TaskTracker("task_tracker.json")
    
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [arguments]")
        sys.exit(1)
        
    command = sys.argv[1]
    if command == "add":
        description = " ".join(sys.argv[2:])
        task_tracker.add_task(description)
    elif command == "update":
        id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        task_tracker.update_task(id, description)
    elif command == "delete":
        id = int(sys.argv[2])
        task_tracker.delete_task(id)
    elif command == "mark-in-progress":
        id = int(sys.argv[2])
        task_tracker.mark_in_progress(id)
    elif command == "mark-done":
        id = int(sys.argv[2])
        task_tracker.mark_done(id)
    elif command == "list": 
        status = sys.argv[2] if len(sys.argv) > 2 else None
        task_tracker.list_tasks(status)       

if __name__ == "__main__":
    main()