from tkinter import * # type: ignore
root = Tk()

def greet():
    a=e1.get()
    b=e2.get()
    l3.config(text=f"Hello {a} {b}!")
    
root.title("Greetings")    
l1 = Label(root, text="Name: ")
l2 = Label(root, text="Surname: ")

e1=Entry(root)
e2=Entry(root)
b = Button(root, text="Greet", command=greet)

l3 = Label(root, text="")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b.grid(row=2, column=0, columnspan=4)

l3.grid(row=3, column=0, columnspan=2)

root.mainloop()