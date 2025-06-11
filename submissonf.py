from tkinter import *  # type: ignore
import re
from tkinter import messagebox  # type: ignore

root = Tk()
root.title("Registration Form")
root.geometry("400x350")
root.resizable(False, False)

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not name or not email or not password:
        messagebox.showwarning("Error", "All fields are required.")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning("Error", "Invalid email format.")
        return
    
    if len(password) < 6:
        messagebox.showwarning("Error", "Password must be at least 6 characters long.")
        return
    
    messagebox.showinfo("Success", f"Registration successful!\nWelcome, {name}.")
        
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

l1 = Label(root, text="Name:", font=("Arial", 12)).pack(pady=(20, 5))
name_entry = Entry(root, width=30)
name_entry.pack()

l2 = Label(root, text="Email:", font=("Arial", 12)).pack(pady=5)
email_entry = Entry(root, width=30)
email_entry.pack()

l3 = Label(root, text="Password:", font=("Arial", 12)).pack(pady=5)
password_entry = Entry(root, width=30, show='*')
password_entry.pack()

b = Button(root, command=submit_form, text="Register", bg="#4CAF50", fg="white", width=15).pack(pady=20)

root.mainloop()