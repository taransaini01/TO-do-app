# To-do-list
tasks=[]

def show_menu():
    print("\n---To-do-List---")
    print("1.Add Task")
    print("2.View Task")
    print("3.Mark as done")
    print("4.Delete Task")
    print("5.Exit")

def add_task():
    task=input("Enter your Task:")
    tasks.append({"task":task,"done":False})
    print(f"Task '{task}' has been added successfully")

def view_task():
    if not tasks:
        print("No tasks yet!")
        return
    for index,task in enumerate(tasks,start=1):
        status="Completed" if task["done"] else "Pending"
        print(f"{index}.{task['task']}[{status}]")

def mark_done():
    if not tasks:
        print("No tasks Yet!")
        return
    view_task()
    try:
        index=int(input("Enter task number:"))-1
        if 0<=index<len(tasks):
            tasks[index]["done"]=True
            print("Marked as done!")
        else:
            print("It is invalid number")
    except:
        print("It is invalid input . please try again")

def delete_task():
    if not tasks:
        print("No tasks yet!")
        return
    view_task()
    try:
        index=int(input("Enter Task number to delete"))-1
        if 0<=index<len(tasks):
            removed=tasks.pop(index)
            print(f"Task '{removed['task']} has deleted")
        else:
            print("Enter valid number sir ")
    except:
        print("The input is invalid . please try again ")

while True:
    show_menu()
    choice=input("Please enter your number(1-5):")
    if choice =='1':
        add_task()
    elif choice=='2':
        view_task()
        input("Press enter to leave")
    elif choice=='3':
        mark_done()
        input("Press enter to leave")
    elif choice=='4':
        delete_task()
        input("Press enter to leave")
    elif choice=='5':
        print("Goodbye")
        break
    else:
        print("Please enter valid number")


