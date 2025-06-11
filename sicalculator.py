from tkinter import *  # type: ignore

root = Tk()

def calculate_interest():
    try:
        principal = float(e1.get())
        rate = float(e2.get())
        time = float(e3.get())
        interest = (principal * rate * time) / 100
        l4.config(text=f"Simple Interest: {interest:.2f}")
    except ValueError:
        l4.config(text="Invalid input! Please enter numbers.")

root.title("Simple Interest Calculator")

l1 = Label(root, text="Principal: ")
l2 = Label(root, text="Rate (%): ")
l3 = Label(root, text="Time: ")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

b = Button(root, text="Calculate", command=calculate_interest)

l4 = Label(root, text="")

# Layout
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1)
b.grid(row=3, column=0, columnspan=2)
l4.grid(row=4, column=0, columnspan=2)

root.mainloop()