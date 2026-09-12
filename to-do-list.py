# To-do-list
from database import create_table,show_tasks,insert_tasks,mark_completed,delete_tasks
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
create_table()
while True:
    show_menu()
    choice=input("Please enter your number(1-5):")
    if choice =='1':
        insert_tasks()
    elif choice=='2':
        show_tasks()
        input("Press enter to leave")
    elif choice=='3':
        mark_completed()
        input("Press enter to leave")
    elif choice=='4':
        delete_tasks()
        input("Press enter to leave")
    elif choice=='5':
        print("Goodbye")
        break
    else:
        print("Please enter valid number")


