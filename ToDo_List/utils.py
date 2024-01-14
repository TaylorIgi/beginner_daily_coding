class Task:
    def __init__(self, id, name, priority):
        
        self.id = id
        self.name = name
        self.priority = priority

    tasks = []

    def include_task(self):
        Task.tasks.append(self)

    def delete_task(self):
        print("Work in progress")

    @staticmethod
    def all_tasks():
        return Task.tasks