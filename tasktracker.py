import json
import os

from task import Task

class TaskTracker:
    def __init__(self, file_name="task_tracker.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []
        
        with open(self.file_name, "r") as file:
            data = file.read()
            if not data:  # Check if file is empty
                return []
            
            try:
                tasks_data = json.loads(data)
                return [Task(task["id"], task["description"], task["status"]) for task in tasks_data]
            except json.JSONDecodeError as e:
                print(f"Error loading tasks: {e}")
                return []

    def save_tasks(self):
        task_data = [task.to_dict() for task in self.tasks]
        with open(self.file_name, "w") as file:
            json.dump(task_data, file, indent=4)
            
    def add_task(self, description, status="todo"):
        task = Task(len(self.tasks) + 1, description, status)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task.id})")
    
    def update_task(self, task_id, description=None, status=None):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            task.update(description, status)
            self.save_tasks()
            print(f"Task updated successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")
            
    def delete_task(self, task_id):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")
            
    def mark_in_progress(self, task_id):
        self.update_task(task_id, status="in-progress")
        
    def mark_done(self, task_id):
        self.update_task(task_id, status="done")
        
    def update_task_status(self, task_id, status):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            task.update(status=status)
            self.save_tasks()
            print(f"Task status updated successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")
            
    def list_tasks(self, status=None):
        if status:
            tasks = [task for task in self.tasks if task.status == status]
        else:
            tasks = self.tasks
        for task in tasks:
            print(task)
    
    