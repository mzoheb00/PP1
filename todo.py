def task():
    tasks = []#empty list
    print("\n-------Welcome to the Task Management App-------\n")
    
    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
        
    # print("Today's tasks are\n {task}")
    
    while True:
        operation = int(input("\nEnter your choice\n\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n\n"))
        if operation == 1:
            add = input("Enter task= ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
            
        elif operation == 2:
            updated_val = input("Enter the task name to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up 
                print(f"Updated task{up}")
        elif operation == 3:
            del_val = input("Which one to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
        elif operation == 4:
            print(f"Total task = {tasks}")
        elif operation == 5:
            print("Closing the Program...")
            break
        else:
            print("Invalid Input!")
task()