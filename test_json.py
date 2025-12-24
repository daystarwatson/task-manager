import json as jsonlib
import os

FILE_NAME = "tasks.json"


def show_menu():
    print("\n TASK MANAGER")
    print("1. view tasks")
    print("2. add task")
    print("3. update task")
    print("4. delete task")
    print("5. EXIT")


def view_tasks(tasks):
    if not tasks:
        print("no tasks available.")
    else:
        for task in tasks:
            print(tasks)


def add_task(tasks):
    title = input("enter task title: ")
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "complete": False
    }
    tasks.append(new_task)
    print(f"task added: {title}")


def update_task(tasks):
    task_id = int(input("enter task id to update: "))
    for task in tasks:
        if task["id"] == task_id:
            task["complete"] = True


def delete_task(tasks):
    task_id = int(input("enter task id to delete: "))
    tasks = [task for task in tasks if task["id"] != task_id]


def save_task(tasks):
    with open("tasks.json", "w") as file:
        jsonlib.dump(tasks, file)


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open("tasks.json", "r") as file:
            try:
                return jsonlib.load(file)
            except jsonlib.JSONDecodeError:
                return []
    return []


def main():

    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("choose an option: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_task(tasks)

        elif choice == "3":
            update_task(tasks)
            save_task(tasks)

        elif choice == "4":
            delete_task(tasks)
            save_task(tasks)

        elif choice == "5":
            save_task(tasks)
            print("good bye")
            break
        else:
            print("invalid choice")


main()
