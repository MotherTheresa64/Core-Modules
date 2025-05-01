# todo_app.py
"""
To-Do List CLI Application
Module 1 Project – Coding Temple
Author: Noah Ragan
"""

def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("Cannot add an empty task.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Thanks for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
