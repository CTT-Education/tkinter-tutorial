from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="look! I clicked a Button!")
    myLabel.pack()
 

myButton = Button(root, text="Click me!", command=myClick, bg='blue')
myButton.pack()

root.mainloop()

