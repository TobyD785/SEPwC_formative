"""
todo.py is a simple python script that
keeps a list in a text file

users may read, add or remove tasks
"""
import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task

    Input - a task to add to the list
    Return - nothing
    """

    with open(TASK_FILE, "a", encoding="utf-8") as f:
#insert text at the end of the file
        f.write(task + "\n")

def list_tasks():
    """Function: list_tasks

    Return - a string of numbered tasks
    """

    if not os.path.exists(TASK_FILE):
#checking file exists
        return ""

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        read = f.readlines()

    listing = "\n".join(f"{i+1}. {task.strip()}" for i, task in enumerate(read) if task.strip())
#combines and numbers tasks
    return listing

def remove_task(index):
    """Function: remove_task

    Input - index of the task to remove
    Return - nothing
    """

    if not os.path.exists(TASK_FILE):
        return

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        tasks = f.readlines()

    if index <= 0 or index > len(tasks):
#ensuring the task exists to remove
        return

    del tasks[index - 1]

    with open(TASK_FILE, "w", encoding="utf-8") as f:
        f.writelines(tasks)
#rewiting the list without the removed task

    return

def main():
    """
    Function: main
    
    Input - nothing
    Return - nothing
    """
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
