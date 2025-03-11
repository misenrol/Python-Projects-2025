import os

def options(username): #options to select your program

    title = f"Welcome to your To-Do-List {username.capitalize()}"
    print(f"{title.center(50, '=')}")
    print("")
    op = "Select your options"
    print(f"{op.center(50, '=')}")
    print("1. Add Tasks")
    print("2. Read Tasks")
    print("3. Delete All Tasks")
    print("4. Exit Program")

def menu(): #main menu
    global tasks
    username = os.getlogin()
    options(username)

    while True:
        print("")
        option = int(input("Enter your number(Type '5' to remind you the options): "))
        if option == 1:
            add_tasks()
            continue

        elif option == 2:
            read_tasks()

        elif option == 3:
            print("")
            file_del_title = "WARNING SAYING Y WILL DELETE THE FILES"
            print(f"{file_del_title.center(50, '=')}")
            print("")
            anwser = input("Are you sure you want to delete ALL your tasks?(Y/N) ").capitalize()
            print("")
            if anwser == "Y":
                try:
                    delete_task()

                except FileNotFoundError:
                    print("There are no files to delete!")
    
            elif anwser == "N":
                menu()
            else:
                print("Invalid option, Y for Yes or N for No")

        elif option == 4: #exit the program
            print("")
            goodbye = "See you next time, goodbye!"
            print(f"{goodbye.center(50, '=')}")
            exit()
        
        elif option == 5:
          options(username)

        else:
            print("Input is invalid")
            

def add_tasks(filename = "tasks.txt"): #adding tasks function(1)
    global tasks
    tasks = []
    add_title = "Let's add a task"
    print(f"{add_title.center(50, '=')}")
    print("Write your task, type 'finshed', to confirm your tasks")
    while True:
        task = input("- ")
        if task.lower() == "finshed":
            break
        tasks.append(task)


    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    
    print(f"Your task has been successfully written!")

def read_tasks(filename = "tasks.txt"): #reading tasks(2)
    try:
        with open(filename, "r") as f:
            tasks = f.readlines()
            your_tasks = "Your Tasks"
            print(f"{your_tasks.center(50, '=')}")
            for task in tasks:
                print(f"- {task.strip()}")

    except FileNotFoundError:
        print("You have no files! Try adding one, by pressing '1'!")

def delete_task(): #deleting tasks(3)
    os.remove("tasks.txt")


menu()
