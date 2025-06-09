from tkinter import *  # type: ignore
root = Tk()
root.title("GUI")
root.geometry("300x200")
f = Frame (root, width=200,height=150,bg="lightblue")

l = Label(root, text = "This is my label widget")
b = Button(f, text = "Click Me")
e=Entry(f)
l.grid(row=0, column=0)
f.grid(row=3, column=0)

b.pack()
e.pack()

root.mainloop()
