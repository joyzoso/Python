#!/usr/bin/python3
# entry.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

#package
from tkinter import *
#module
from tkinter import ttk        
    
root = Tk()

#calling module and the entry constructor method
#(enter widget for one line of text and text widget for multiple)
entry = ttk.Entry(root, width = 30)
#pack method to scale out the GUI
entry.pack()

#using get as opposed to bing to retrieve contents of the entry field
entry.get()
#will delete the first letter of entry field
entry.delete(0, 1)
#will delete the last letter of entry field
entry.delete(0, END)

entry.insert(0, 'Enter your password')

#using show property and passes an asterick instead of an actual password, etc...
entry.config(show = '*')
#grey's out the text box
entry.state(['disabled'])
#readonly state, cannot enter anything, but copy something
entry.state(['readonly'])
entry.state(['!disabled'])

root.mainloop()
