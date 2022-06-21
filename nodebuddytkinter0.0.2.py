# Program to make a simple
# login screen 
 
 
import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing volt
volt_var=tk.StringVar()

 
  
# defining a function that will
# get the volt
# print them on the screen
def submit():
    volt=volt_var.get()
    if volt== int(1)
    voltagelabel = tk.Label(root, text=volt).grid(row=3, column=0)
     
    volt_var.set("")
    print(volt)

     
     
# creating a label for
# volt using widget Label
volt_label = tk.Label(root, text = 'Voltage', font=('calibre',10, 'bold'))
  
# creating a entry for input
# volt using widget Entry
volt_entry = tk.Entry(root,textvariable = volt_var, font=('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
volt_label.grid(row=0,column=0)
volt_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()