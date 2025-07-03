def manage_tasks(tasks):
    operation = input(
        "Enter 'a' to add a task, 'd' to delete a task, or 'q' to quit: ")

    if operation.lower() == 'a':
        while True:
            task = input("Enter a task (q to quit): ")
            if task.lower() == 'q':
                print("The tasks are recorded")
                break
            tasks.append(task)
            print(f"Task '{task}' has been added.")

    elif operation.lower() == 'd':
        if not tasks:
            print("No tasks to delete.")
            return tasks
        for task in tasks:
            print(task)
        task_to_delete = input("Enter the task you want to delete: ")
        if task_to_delete in tasks:
            tasks.remove(task_to_delete)
            print(f"Task '{task_to_delete}' has been deleted.")
        else:
            print(f"Task '{task_to_delete}' not found.")

    elif operation.lower() == 'q':
        print("Exiting the task manager. Goodbye!")

    else:
        print("Invalid operation. Please enter 'a', 'd', or 'q'.")

    for_tasks_print = input("Do you want to print the tasks? (y/n): ")
    if for_tasks_print.lower() == 'y':
        for task in tasks:
            print(task)

    return tasks


def main():
    print("Welcome to the Task Manager!")
    tasks = []

    while True:
        tasks = manage_tasks(tasks)
        if not tasks:
            print("No tasks available.")
        else:
            print("Current tasks:")
            for task in tasks:
                print(f"- {task}")

        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            print("Exiting the Task Manager. Goodbye!")
            break


main()
