import utils
import os

action = 0

while action != 4:

    action = utils.show_menu()

    if action == 1:
        utils.user_create_task()
    elif action == 2:
        utils.user_delete_task()
    elif action == 3:
        utils.show_tasks_table(utils.Task.list_all_tasks())

os.system("cls")