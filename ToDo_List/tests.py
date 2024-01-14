import utils
import os
import time
from prettytable import PrettyTable as pt
        
utils.Task(utils.Task.get_max_id()+1, "Estudar", "High").include_task()
utils.Task(utils.Task.get_max_id()+1, "Comprar pão", "Low").include_task()

tasks_table = pt()
tasks_table.field_names = ["Task_ID", "Description", "Priority"]

for my_task in utils.Task.list_all_tasks():
    tasks_table.add_row([my_task.id, my_task.description, my_task.priority])

print(tasks_table)

