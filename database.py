# making a database to do list 
# using a database to store the tasks instead of a list
import sqlite3
def create_table():
    conn=sqlite3.connect('Task_manager')
    c=conn.cursor()
    c.execute("""create table if not exists Tasks (
    task_name varchar(50),
    task_status varchar(50))

    """)
  
    conn.commit()
    conn.close()    

def insert_tasks():
    conn=sqlite3.connect('Task_manager')
    c=conn.cursor()
    tasks=input("Enter your task:")
    status="Pending"
    c.execute("""insert into Tasks (task_name,task_status) values(?,?)

    """,(tasks,status))
    print(f"Task {tasks} has been added successfully")
    conn.commit()
    conn.close()

def show_tasks():
    conn=sqlite3.connect('Task_manager')
    c=conn.cursor()
    c.execute("""select rowid,* from Tasks
    order by rowid

    """)
    items=c.fetchall()
    if not items:
        print("No tasks Found....")
    else:
        for item in items:
            print(item)
    conn.close() 

def mark_completed():
    conn=sqlite3.connect('Task_manager')
    c=conn.cursor()
    task_id=input("Enter your task number:")
    c.execute("""update Tasks 
    set task_status=?
    where rowid=?

    """,("Completed",task_id))
    if c.rowcount==0:
        print("No task found with that id ")
    else:
        print("Task marked as completed")
    conn.commit()
    conn.close()     

def delete_tasks():
    show_tasks()
    task_id=input("Enter your task number to delete")
    conn=sqlite3.connect('Task_manager')
    c=conn.cursor()
    c.execute(""" delete from Tasks 
    where rowid=?
   
    """,(task_id,))
    if c.rowcount==0:
        print("No task found with that id")
    else:
        print("Your task has been deleted")
    conn.commit()
    conn.close()






