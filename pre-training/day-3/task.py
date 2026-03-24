from datetime import datetime

class Task:
    def __init__(self, id, title, status='todo'):
        self.id = id
        self.title =  title
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
       task = cls(data["id"], data["title"], data.get("status", "todo"))
       task.created_at = data.get("created_at")
       return task
    
