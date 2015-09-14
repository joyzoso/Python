#!/usr/bin/python3
# selection_boxes.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#create a string variable to store values from combo box
month = StringVar()
#using tk modules themed combo box constructor method
combobox = ttk.Combobox(root, textvariable = month)
#geometry manager to place it
combobox.pack()
#config method and passing in list
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
##get value that is currently in the box
print(month.get())
#use set method to change value
month.set('Dec')
#another example
month.set('Not a month!')

#spin box, creating another variable year
year = StringVar()
#just use spinbox and pass in parameters
#note the underscore because from is a protected keyword
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
print(year.get())

root.mainloop()
