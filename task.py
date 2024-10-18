import datetime

class Task:
    
    def __init__(self, id, description, status="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return f"Task({self.id}, {self.description}, {self.status}, {self.created_at}, {self.updated_at})"

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
    def update(self, description=None, status=None):
        if description:
            self.description = description
        if status:
            self.status = status
        self.updated_at = datetime.datetime.now().isoformat()