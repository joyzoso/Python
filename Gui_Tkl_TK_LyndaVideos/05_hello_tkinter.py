#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

#tk constructor window
from tkinter import * 

#tk constructor method creates main window, widget and assigns it the variable named root
root = Tk()
#create a label with the text as a child of the root window and using the pack method to put it in the window
Label(root, text="Hello, Tkinter!").pack()
#running the main loop method for the root window
root.mainloop()
