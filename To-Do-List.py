# Simple Command Line To-Do List Manager
# Useful for managing daily tasks and practicing Python basics.

def display_tasks(task_list):
    if not task_list:
        print("\nYour task list is empty!")
    else:
        print("\n--- CURRENT TASKS ---")
        for position, current_task in enumerate(task_list, 1):
            print(f"{position}. {current_task}")

def run_todo_app():
    task_list = []
    while True:
        print("\n1. View tasks\n2. Add task\n3. Delete task\n4. Exit")
        user_choice = input("Choose an option (1-4): ").strip()
        
        if user_choice == "1":
            display_tasks(task_list)
        elif user_choice == "2":
            new_task_item = input("Enter the new task: ").strip()
            if new_task_item:
                task_list.append(new_task_item)
                print(f"Task added: '{new_task_item}'")
        elif user_choice == "3":
            display_tasks(task_list)
            if task_list:
                try:
                    task_index = int(input("Enter the number of the task to remove: "))
                    if 1 <= task_index <= len(task_list):
                        removed_item = task_list.pop(task_index - 1)
                        print(f"Removed task: '{removed_item}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif user_choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    run_todo_app()