from tkinter import *  # type: ignore
from tkinter import messagebox  # type: ignore

def add_task () :
    task = entry.get()
    if task: 
        task_listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
def delete_task () :
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")
        
root = Tk()
root.title("To-Do List")
task_listbox = Listbox(root, width=50, height=10, bd=2, selectbackground="grey")
task_listbox.pack(pady=10,fill=BOTH)

entry  = Entry(root, width=50, bg ="lightblue", fg="red")
entry.pack(pady=10)

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()

