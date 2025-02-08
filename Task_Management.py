def task():
    tasks = [] # empty list
    print("-------Welcome to the Task Managment App-------")

    total_task = int(input("Enter how many task you want to add : "))

    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
        if operation == 1:
            new_task = input("Enter task name : ")
            tasks.append(new_task)
            print(f"Task {new_task} successefully added")
        elif operation == 2:
            update_val = input("Enter task you want to update : ")
            if update_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"updated Task {up}")
            else:
                print("Task not present in the task list")
        elif operation == 3:
            del_task = input("Enter task name which you want delete : ")
            if del_task in tasks:
                ind = tasks.index(del_task)
                del tasks[ind]
                print(f"Task is {del_task} successefully deleted")
            else:
                print(f"{del_task} is not present in the task list")
        elif operation == 4:
            print(f"Total Task {tasks}")
        elif operation == 5:
            print("Closing the program............")
            break
        else:
            print("Invalid choice ")
        

task()