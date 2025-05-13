# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import datetime as date


task_items = {}
file_name = "task.json"


def adding_task(descript, task_ids, file):
    global task_items
    status = "Todo"
    try:
        with open(file, "r") as f:
            task_item = json.load(f)
    except FileNotFoundError:
        print("Does not Exist")
        task_item = {}
# Add new task
    timestamp = date.datetime.now().isoformat(" ", "seconds")
    task_item[task_ids] = {
        "Description": descript,
        "status": status,
        "time": timestamp
    }

# Write updated tasks to file
    with open(file, "w") as f:
        json.dump(task_item, f, indent=4)
        print("Task Added successfully")




def all_task(file):
    try:
        with open(file, "r") as f:
            task_items = json.load(f)
    except FileNotFoundError:
        print("Does not Exist")

    for ids, task_info in task_items.items():
        print(f"number: {ids}, Info: {task_info['Description']}, Status: {task_info['status']}, Date: {task_info['time']}")



def update_task(file, update_id):
    try:
        with open(file, "r") as f:
            task_item = json.load(f)
    except FileExistsError:
        print("File already exist")

    if update_id not in task_item:
        print("Does not have the task")
        return

    change_id = input("Change: 1 for complete, 2 for Not Done: ").strip()

    if change_id == '1':
        task_items[update_id]['status'] = "Complete"
    elif change_id == '2':
# adding Not Done status in the specific ids in the task items
        task_items[update_id]['status'] = "not Done"
        return
    else:
        print("Invalid Input")
    with open(file_name, "w") as f:
        json.dump(task_items, f, indent=4)
        print("Status Updated Successfully")

def delete_task(file, ids):
    task_ids = ids
    try:
        with open(file, "r") as f:
            task_item = json.load(f)
    except FileExistsError:
        print("File already exist")

    while True:
        if task_ids in task_item:
            del task_items[task_ids]
            with open(file_name, "w") as f:
                json.dump(task_items, f, indent=4)
            print(f"Task {task_ids} Delete Successfully")
            break
        else:
            print("Task Id not found")
            task_ids = input("Enter the Valid Id to delete: ")





while True:
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Mark Task")
    print("5. List of Task")
    print("6. List of Done Task")
    print("7. List of Not Done Task")
    print("8. List of In Progress Task")
    print("9. Exit")
    choice = input("Enter your Choice: ").lower().strip()
    if choice == '1':
        task_descript = input("Enter Task to Add: ")
        task_id = str(len(task_items) + 1)
        adding_task(task_descript, task_id, file_name)
    elif choice == '2':
        print("All Task choose to update")
        all_task(file_name)
        update_choice = str(input("Choose a number to change Status: "))
        update_task(file_name, update_choice)


    elif choice == '3':
        print("List of All Task")
        all_task(file_name)
        id_choice = input("Enter the Id to Delete : ")
        delete_task(file_name, id_choice)


    elif choice == '4':
        print("List of All Task")
        all_task(file_name)
        back = input("y to back: ").lower()
        if back != 'y':
            print("List of All Task")
            all_task(file_name)
            back = input("y to back: ")

    elif choice == '5':
        print("List of  Task")
        all_task(file_name)
        back = input("y to back: ").lower()
        if back != 'y':
            print("List of All Task")
            all_task(file_name)
            back = input("y to back: ")


