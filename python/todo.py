import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    
    with open(TASK_FILE, "a") as f:    #text is inserted at the end of the file
        f.write(task + "\n")

def list_tasks():
    """Function: list_tasks
    
    Return - a string of numbered tasks
    """
    
    if not os.path.exists(TASK_FILE):    #checking file exists
        return ""
    
    with open(TASK_FILE, "r") as f:    
        read = f.readlines()
        
    return "\n".join(f"{i+1}. {task.strip()}" for i, task in enumerate(read)).strip()    #combines and numbers tasks

def remove_task(index):
    """Function: remove_task
    
    Input - index of the task to remove
    Return - nothing
    """
    
    if not os.path.exists(TASK_FILE):
        return

    with open(TASK_FILE, "r") as f:
        tasks = f.readlines()
        
    if index <= 0 or index > len(tasks):    #ensuring the task exists to remove
        return
    
    del tasks[index - 1]
    
    with open(TASK_FILE, "w") as f:
        f.writelines(tasks)    #rewiting the list without the removed task

    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
