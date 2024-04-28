class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

    def mark_complete(self, task_number):
        try:
            self.tasks[task_number - 1] = f"{self.tasks[task_number - 1]} (Completed)"
        except IndexError:
            print("Invalid task number.")

    def unmark_complete(self, task_number):
        try:
            task = self.tasks[task_number - 1]
            if "Completed" in task:
                self.tasks[task_number - 1] = task.replace(" (Completed)", "")
            else:
                print("Task is not marked as complete.")
        except IndexError:
            print("Invalid task number.")

    def edit_task(self, task_number, new_task):
        try:
            self.tasks[task_number - 1] = new_task
        except IndexError:
            print("Invalid task number.")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task}\n")

    def load_from_file(self, filename):
        self.tasks = []
        with open(filename, 'r') as f:
            for line in f:
                task = line.strip()
                self.tasks.append(task)

my_list = ToDoList()

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark complete")
    print("5. Unmark complete")
    print("6. Edit task")
    print("7. Save to file")
    print("8. Load from file")
    print("9. Quit")

    option = int(input("Enter an option: "))

    if option == 1:
        task = input("Enter a task: ")
        my_list.add_task(task)
    elif option == 2:
        my_list.view_tasks()
    elif option == 3:
        task_number = int(input("Enter the task number to delete: "))
        my_list.delete_task(task_number)
    elif option == 4:
        task_number = int(input("Enter the task number to mark as complete: "))
        my_list.mark_complete(task_number)
    elif option == 5:
        task_number = int(input("Enter the task number to unmark as complete: "))
        my_list.unmark_complete(task_number)
    elif option == 6:
        task_number = int(input("Enter the task number to edit: "))
        new_task = input("Enter the new task: ")
        my_list.edit_task(task_number, new_task)
    elif option == 7:
        filename = input("Enter the filename to save to: ")
        my_list.save_to_file(filename)
    elif option == 8:
        filename = input("Enter the filename to load from: ")
        my_list.load_from_file(filename)
    elif option == 9:
        break
    else:
        print("Invalid option. Try again.")
