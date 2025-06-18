from tkinter import * #type: ignore
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=6)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

b1=Button(root, text="1", padx=40, pady=20)
b2=Button(root, text="2", padx=40, pady=20)
b3=Button(root, text="3", padx=40, pady=20)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

def b_add():
    firstnum=e.get()
    global f_num
    global sym
    sym='+'
    f_num=int(firstnum)
    e.delete(0, END)
    
def buttoneq():
    secnum=e.get()
    e.delete(0, END)
    if sym == '+':
        e.insert(0, str(f_num + int(secnum)))
    elif sym == '-':
        e.insert(0, str(f_num - int(secnum)))
    elif sym == '*':
        e.insert(0, str(f_num * int(secnum)))
    elif sym == '/':
        e.insert(0, str(f_num / int(secnum)))

def buttonclear():
    e.delete(0, END)
    
bclear=Button(root, text='Clear', padx=30, pady=20, command=buttonclear)
bclear.grid(row=6,column=0)

b1=Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
b2=Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
b3=Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
b4=Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
b5=Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
b6=Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
b7=Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
b8=Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
b9=Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
b0=Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))
bclear=Button(root, text='Clear', padx=30, pady=20, command=buttonclear)

badd=Button(root,text='+', padx=40, pady=20)
bsub=Button(root, text='-', padx=40, pady=20)
bmulti=Button(root, text='*', padx=40, pady=20)
bdiv=Button(root, text='/', padx=40, pady=20, command=b_add)
beq=Button(root, text='=', padx=40, pady=20)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

bsub.grid(row=4, column=0)
bmulti.grid(row=4, column=1)
bdiv.grid(row=4, column=2)

badd.grid(row=5, column=1)
beq.grid(row=5, column=2)
b0.grid(row=5, column=0)

bclear.grid(row=6, column=0)

root.mainloop()

