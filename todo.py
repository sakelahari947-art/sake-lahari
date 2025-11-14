import os
# --- Constants ---
TODO_FILE = "todo.txt"

# --- Core Functions ---

def load_tasks():
    """Loads tasks from the todo file into a list."""
    tasks = []
    # Check if the file exists to avoid FileNotFoundError
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            # Read each line, strip leading/trailing whitespace, and add to the list
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Saves the current list of tasks back to the todo file."""
    with open(TODO_FILE, 'w') as file:
        # Write each task on a new line
        for task in tasks:
            file.write(f"{task}\n")
# --- Functionality Implementation ---

def view_tasks(tasks):
    """Displays all current tasks with their indices."""
    if not tasks:
        print("\n📝 Your To-Do List is empty!")
        return

    print("\n✅ Current To-Do List:")
    # Use enumerate to display index (starting at 1 for user-friendliness)
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    print("-" * 30)

def add_task(tasks):
    """Prompts the user for a new task and adds it to the list."""
    task = input("\n➕ Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Task added: "{task}"')
    else:
        print("Task cannot be empty.")
def remove_task(tasks):
    """Prompts for a task number and removes it from the list."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        # Prompt for the index to remove (user input is 1-based)
        task_num = int(input("\n➖ Enter the number of the task to remove: "))
        
        # Convert user's 1-based index to 0-based list index
        index_to_remove = task_num - 1
        
        # Validate the index
        if 0 <= index_to_remove < len(tasks):
            removed_task = tasks.pop(index_to_remove)
            save_tasks(tasks)
            print(f'Task removed: "{removed_task}"')
        else:
            print(f"Invalid task number: {task_num}. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
# --- Main Application Loop ---

def main():
    """The main function to run the application."""
    tasks = load_tasks() # Load existing tasks on startup

    print("--- 🚀 Welcome to the Console To-Do List App! ---")

    while True:
        print("\n\n--- Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\n👋 Saving tasks and exiting. Goodbye!")
            # Tasks are saved in add_task and remove_task, but calling it here is a safe final step
            save_tasks(tasks) 
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()