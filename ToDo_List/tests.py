import utils
import os
import time
from prettytable import PrettyTable as pt
        
utils.Task(1, "Estudar", "High").include_task()
utils.Task(2, "Comprar pão", "Low").include_task()

tasks_table = pt()
tasks_table.field_names = ["Task_ID", "Description", "Priority"]

for my_task in utils.Task.all_tasks():
    tasks_table.add_row([my_task.id, my_task.name, my_task.priority])

print(tasks_table)

