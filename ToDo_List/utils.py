import os
import time

class Task:
    
    def __init__(self, id, description, priority):
        
        self.id = id
        self.description = description
        self.priority = priority

    tasks = []

    def include_task(self):
        Task.tasks.append(self)
        print(f"Task included! (ID: {self.id} | Description: {self.description}) | Priority: {self.priority}")
        time.sleep(3)

    def delete_task(id):
        for my_task in Task.tasks:
            if my_task.id == id:
                my_task_description = my_task.description
                Task.tasks.remove(my_task)
                print(f"Task deleted (ID: {id} | Description: {my_task_description})")
            else:
                print(f"Task ID {id} not found.")
        time.sleep(3)

    @staticmethod
    def list_all_tasks():
        return Task.tasks
    
    @staticmethod
    def get_max_id():
        if not Task.tasks:
            return -1
        return  max(task.id for task in Task.tasks)
    
def show_menu():
    os.system("cls")
    print("-"*40)
    print("Choose an option:\n")
    print("1 - Create a task")
    print("2 - Delete a task")
    print("3 - List all tasks")
    print("-"*40)