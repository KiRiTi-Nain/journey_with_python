

def display_todo_list(todo_list):
    print("Todo List:")
    if not todo_list:
        print("No tasks.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the todo list.")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the todo list.")
    else:
        print("Invalid task index.")

def main():
    todo_list = []

    while True:
        display_todo_list(todo_list)
        print("\nCommands:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == '3':
            print("Exiting todo list.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
