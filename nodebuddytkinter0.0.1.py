from cProfile import label
from tkinter import *

root = Tk()
root.title("Node Buddy")

label1 = Label(root, text="Please Enter Node Voltage").grid(row=0, column=0)
voltageentry = Entry(root).grid(row=0, column=1)

def calculation():
    voltage=volt_var.get()

    volt_var.set("")


button_1 = Button(root, text="Calculate").grid(row=1, column=0)



root.mainloop()