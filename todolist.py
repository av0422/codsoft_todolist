#TASK 1 'TO DO LIST'

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def save_tasks(self):
        with open('tasks.txt', 'w') as tasks_file:
            for task in self.tasks:
                tasks_file.write(task + '\n')

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as tasks_file:
                self.tasks = [task.strip() for task in tasks_file.readlines()]
        except FileNotFoundError:
            pass


def main():
    todo_list = TodoList()
    todo_list.load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            todo_list.save_tasks()

        elif choice == '2':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
            todo_list.save_tasks()

        elif choice == '3':
            todo_list.display_tasks()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
