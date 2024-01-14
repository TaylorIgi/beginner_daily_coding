import os
import time
from prettytable import PrettyTable as pt

class Task:
    
    def __init__(self, id, description, priority):       
        self.id = id
        self.description = description
        self.priority = priority

    tasks = []

    def include_task(self):
        os.system("cls")
        Task.tasks.append(self)
        print(f"Task included!\nID: {self.id} | Description: {self.description} | Priority: {self.priority}")
        time.sleep(3)

    def delete_task(id):
        my_task_description = ""
        for my_task in Task.tasks:
            if my_task.id == id:
                my_task_description = my_task.description
                Task.tasks.remove(my_task)
                print(f"Task deleted\nID: {id} | Description: {my_task_description}")
        if my_task_description == "":
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
    print("4 - Exit")
    print("-"*40)
    return int(input("Type your option number: "))

def show_tasks_table(tasks_list):

    os.system("cls")
    tasks_table = pt()
    tasks_table.field_names = ["Task_ID", "Description", "Priority"]

    for my_task in Task.list_all_tasks():
        tasks_table.add_row([my_task.id, my_task.description, my_task.priority])

    print(tasks_table)
    time.sleep(3)

def user_create_task():
    os.system("cls")
    task_id = Task.get_max_id()+1
    task_description = input("What is the task description? ")
    task_priority = input("Task priority is High, Medium or Low? ").title()
    Task(task_id, task_description, task_priority).include_task()

def user_delete_task():

    Task.delete_task(int(input("What task ID you want to delete? ")))