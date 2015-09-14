#!/usr/bin/python3
# frame.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#frame constructor
frame = ttk.Frame(root)
#pack geometry manager to place the frame within it
frame.pack()
#has a dfault menu, but can use config to set properties
frame.config(height = 100, width = 200)
#6 types of frame styles, use in CAPS
frame.config(relief = RIDGE)
#creating a button widget and using the frame as the parent
ttk.Button(frame, text = 'Click Me').grid()
#adding padding and accepts to values, x and y direction
frame.config(padding = (40, 15))
#create a label frame and it has an additional property of text
ttk.LabelFrame(root, height = 50, width = 200, text = 'My Frame').pack()

root.mainloop()
