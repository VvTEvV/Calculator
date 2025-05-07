from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title("Basic Git & Github By VvTEvV")
GUI.geometry("500x700")

L = Label(GUI,text="VvTEvV") #
L.pack()

L = Label(GUI,text="Username") #
L.pack()

L = Label(GUI,text="Username") #
L.pack()

L = Label(GUI,text="Username") #
L.pack()

v1 = StringVar()
E1 = ttk.Entry(GUI,textvariable=v1)
E1.pack()

v2 = StringVar()
E2 = ttk.Entry(GUI,textvariable=v2)
E2.pack()

def cal():
    c = float(v1.get()) + float(v2.get())
    r1= v1.get()
    r2= v2.get()
    text = f'{r1} + {r2} = {c}'
    messagebox.showinfo("Resule",text)
b1 = ttk.Button(GUI,text='Calculator', command=cal)
b1.pack()

GUI.mainloop()