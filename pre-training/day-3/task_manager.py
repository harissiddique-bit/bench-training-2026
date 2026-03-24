
import json
from task import Task

FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(FILE, "r") as f:
                data = json.load(f)
                tasks = []
                for item in data:
                    tasks.append(Task.from_dict(item))
                return tasks
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("tasks.json file is broken. Starting with empty list.")
            return []

    def save_tasks(self):
        data = []
        for task in self.tasks:
           data.append(task.to_dict())
        with open(FILE, "w") as f:
           json.dump(data, f, indent=2)

    def add_task(self, title):
        if len(self.tasks) == 0:
            new_id = 1
        else:
            new_id = self.tasks[-1].id + 1

        task = Task(new_id, title)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added:", title)

    def complete_task(self, task_id):
        found = False
        for task in self.tasks:
            if task.id == task_id:
                task.status = "done"
                self.save_tasks()
                print("Marked as done:", task.title)
                found = True
                break

        if found == False:
            print("No task found with id", task_id)

    def delete_task(self, task_id):
        found = False
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted:", task.title)
                found = True
                break

        if found == False:
            print("No task found with id", task_id)

    def list_tasks(self, filter=None):
        if filter == "done":
            tasks_to_show = []
            for task in self.tasks:
                if task.status == "done":
                    tasks_to_show.append(task)
        elif filter == "todo":
            tasks_to_show = []
            for task in self.tasks:
                if task.status == "todo":
                    tasks_to_show.append(task)
        else:
            tasks_to_show = self.tasks

        if len(tasks_to_show) == 0:
            print("No tasks found.")
            return

        print('---------------------')
        for task in tasks_to_show:
            print(f"[{task.id}] {task.title} - {task.status} - {task.created_at}")
        print('---------------------')
