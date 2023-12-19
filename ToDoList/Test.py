list = []

def display_Tasks(tasks):
    print("Your ToDoList:")
    for index,task in enumerate(tasks,start=1):
        print(f"{index}. {task}")

def add(tasks,task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def main():
    tasks = []
    while True:
        print("\nOptions: add [task],show quit")
        user_input = input("Enter a command: ")

        if user_input == "quit":
            break
        elif user_input == "show":
            display_Tasks(tasks)
        elif user_input.startswith("add "):
            _,task = user_input.split(" ",1)
            add(tasks,task)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()