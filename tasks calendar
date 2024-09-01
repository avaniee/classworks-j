def display_tasks(tasks):
    if tasks:
        print("Your to-do list:")
        for i,task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: {task}")

def main():
    tasks = []
    while True:
        print("\nOptions: ")
        print("1. Display current tasks")
        print("2. Add a task")
        print("3. Exit")
        option = input("Choose an option (1/2/3): ")

        if option == '1':
            display_tasks(tasks)
        elif option == '2':
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif option == '3':
            break
        else:
            print("Invalid option, please try again.")

main()
