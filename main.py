# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import datetime as date


task_items = {}
file_name = "task.json"


def get_next_task_id(file):
    if not os.path.exists( file ) or os.path.getsize( file ) == 0:
        # File missing or empty → start with ID "1"
        return "1"
    try:
        with open(file, "r") as f:
            data = json.load(f)
            if data:
                return str(int(max(data.keys(), key=str)) + 1)
            else:
                return "1"
    except (json.JSONDecodeError,FileNotFoundError):
        return "1"

def adding_task(descript, task_ids, file):
    global task_items
    marked = "Not Done"
    timestamp = date.datetime.now().isoformat( " ", "seconds" )
    try:
        with open(file, "r") as f:
            try:
                task_item = json.load( f )
            except json.JSONDecodeError:
                task_item = {}
    except FileNotFoundError:
        print("Does not Exist")
        task_item = {}

# Add new task
    task_item[task_ids] = {"Description": descript, "Time": timestamp, "Marked": marked
    }
# Write updated tasks to file
    with open(file, "w") as f:
        json.dump(task_item, f, indent=4)
        print("Task Added successfully")




def display_task(file):
    try:
        with open(file, "r") as f:
            task_items = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Does not Exist")
        return

    for ids, task_info in task_items.items():
        print( "===================================" )
        print(f"Task: {ids}, Description: {task_info['Description']}\nDate: {task_info['Time']}\nMarked: {task_info['Marked']}")
        print( "===================================" )



def update_task(file, update):
    try:
        with open(file, "r") as f:
            task_item = json.load(f)
    except FileExistsError:
        print("File already exist")

    if update not in task_item:
        print("Does not have the task")
        return
    else:
        print( "===================================" )
        update_task = input("Enter Updated Task to update: ")
        print( "===================================" )
        timestamp_update = date.datetime.now().isoformat( " ", "seconds" )
        task_item[update]["Description"] = update_task
        task_item[update]["Time"] = timestamp_update
    with open(file_name, "w") as f:
        json.dump(task_item, f, indent=4)
        print(" Update Successfully")
        print( "===================================" )

def delete_task(ids, file):
    task_ids = ids if isinstance(ids, list) else [ids]
    try:
        with open(file, "r") as f:
            task_item = json.load(f)
    except FileNotFoundError:
        print("File already exist")

    for task_id in task_ids:
        if task_id in task_item:
            del task_item[task_id]
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Task {task_id} not found.")


    new_task_items = {}
    sorted_item = sorted(task_item.items(), key = lambda x: int(x[0]))
    for i, (old_id, task_data) in enumerate(sorted_item, start=1):
        new_task_items[str(i)] = task_data

    with open( file, "w" ) as f:
        json.dump( new_task_items, f, indent=4 )



def marked_tasked_inProgress(id, file):
    try:
        with open(file, "r") as f:
            task_items = json.load(f)
    except FileNotFoundError:
        print("File already exist")

    while True:
        if id in task_items:
            marked_inprogress = "In Progress"
            task_items[id]["Marked"] = marked_inprogress


            with open(file, "w") as f:
                json.dump(task_items, f, indent=4)
            print(f"Task {id} Marked Successfully")
            break
        else:
            print( "===================================" )
            print("Task number not found")
            print( "===================================" )
            task_id = input("Enter the Valid Task number to Marked (or type 'cancel' to exit): ").lower()
            print( "===================================" )
            if task_id == 'cancel':
                print( "===================================" )
                print('marked cancelled')
                print( "===================================" )
                break


def marked_tasked_Done(id, file):
    try:
        with open(file, "r") as f:
            task_items = json.load(f)
    except FileNotFoundError:
        print("File already exist")

    while True:
        if id in task_items:
            marked_done = "Done"
            task_items[id]["Marked"] = marked_done


            with open(file, "w") as f:
                json.dump(task_items, f, indent=4)
            print(f"Task {id} Marked Successfully")
            break
        else:
            print( "===================================" )
            print("Task Id not found")
            print( "===================================" )
            task_id = input("Enter the Valid Id to Marked (or type 'cancel' to exit): ").lower()
            print( "===================================" )
            if task_id == 'cancel':
                print( "===================================" )
                print('marked cancelled')
                print( "===================================" )
                break

def display_task_done(file):
    try:
        with open( file, "r" ) as f:
            task_items = json.load( f )
    except (FileNotFoundError, json.JSONDecodeError):
        print( "File already exist" )
        return
    for ids, task_info in task_items.items():
        if task_info.get("Marked", "").strip().lower() == 'done':
            print("===================================")
            print(f"Task: {ids}, Description: {task_info['Description']}\nDate: {task_info['Time']}\nMarked: {task_info['Marked']}")
            print( "===================================" )
        found = True

    if not found:
        print( "No tasks marked as done." )

def display_task_Notdone(file):
    try:
        with open( file, "r" ) as f:
            task_items = json.load( f )
    except (FileNotFoundError, json.JSONDecodeError):
        print( "File already exist" )
        return
    for ids, task_info in task_items.items():
        if task_info.get("Marked", "").strip().lower() == 'not done':
            print( "===================================" )
            print(f"Task: {ids}, Description: {task_info['Description']}\nDate: {task_info['Time']}\nMarked: {task_info['Marked']}")
            print( "===================================" )
        found = True

    if not found:
        print( "No tasks marked as done." )

def display_task_Inprogress(file):
    try:
        with open( file, "r" ) as f:
            task_items = json.load( f )
    except (FileNotFoundError, json.JSONDecodeError):
        print( "File already exist" )
        return
    for ids, task_info in task_items.items():
        if task_info.get("Marked", "").strip().lower() == 'in progress':
            print( "===================================" )
            print(f"Task: {ids}, Description: {task_info['Description']}\nDate: {task_info['Time']}\nMarked: {task_info['Marked']}")
            print( "===================================" )
        found = True

    if not found:
        print( "No tasks marked as done." )



def main():
    while True:
        print( "1. Add Task" )
        print( "2. Update Task" )
        print( "3. Delete Task" )
        print( "4. Mark Task" )
        print( "5. List of Task" )
        print( "6. List of Done Task" )
        print( "7. List of Not Done Task" )
        print( "8. List of In Progress Task" )
        print( "9. Exit" )
        choice = input( "Enter your Choice: " ).lower().strip()
        if choice == '1':
            print( "===================================" )
            task_descript = input( "Enter Task to Add: " )
            print( "===================================" )
            task_id = get_next_task_id( file_name )
            adding_task( task_descript, task_id, file_name )
            print( "===================================" )
        elif choice == '2':
            print( "===================================" )
            print( "All Task choose to update" )
            display_task( file_name )
            update_choice = input( "Choose a Task number to change: " )
            update_task( file_name, update_choice )

        elif choice == '3':
            print( "===================================" )
            print( "List of All Task" )
            display_task( file_name )
            delete_choice = input( "Choose a Task number for multiple delete use (comma-separated): " )
            task_ids = [id.strip() for id in delete_choice.split( "," )]
            cancel = ("(type 'cancel' to exit): ").lower()
            print( "===================================" )
            if cancel == 'cancel':
                print( "delete cancelled" )
                print( "===================================" )
            else:
                delete_task( task_ids, file_name )


        elif choice == '4':
            print( "===================================" )
            print( "List of All Task" )
            display_task( file_name )
            marked_choice = input( "1 – Mark task In Progress 2 – Mark task Done: " )
            print( "===================================" )
            if marked_choice == '1':
                user = input( "Choose the Task number of Task to be Mark as in progress: " )
                marked_tasked_inProgress( user, file_name )
                print( "Marked Successfully" )
                print( "===================================" )
            elif marked_choice == '2':
                user = input( "Choose the  of Task to be Mark as Done: " )
                marked_tasked_Done( user, file_name )
            else:
                print( "===================================" )
                print('Invalid Input')
                print( "===================================" )


        elif choice == '5':
            print( "===================================" )
            print( "List of Task" )
            display_task( file_name )
            back = input( "y to back: " ).upper()
            print( "===================================" )
            if back != 'Y':
                print( "===================================" )
                back = input( "y to back: " )
                print( "===================================" )

        elif choice == '6':
            print( "List of Done Task" )
            display_task_done( file_name )
            back = input( "y to back: " ).upper()
            if back != 'Y':
                print( "===================================" )
                back = input( "y to back: " )
                print( "===================================" )

        elif choice == '7':
            print( "List of Not Done Task" )
            display_task_Notdone( file_name )
            back = input( "y to back: " ).upper()
            if back != 'Y':
                print( "===================================" )
                back = input( "y to back: " )
                print( "===================================" )

        elif choice == '8':
            display_task_Inprogress( file_name )
            back = input( "y to back: " ).upper()
            if back != 'Y':
                print( "===================================" )
                back = input( "y to back: " )
                print( "===================================" )

        elif choice == '9':
            break

        else:
            print( "===================================" )
            print( "Invalid Input" )
            print( "===================================" )


main()




