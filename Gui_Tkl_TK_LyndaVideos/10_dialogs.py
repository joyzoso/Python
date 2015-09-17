#!/usr/bin/python3
# dialogs.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# root widget needed
#only need to import the messagebox module
from tkinter import messagebox

#create a MB and then the name of one of the methods, pass 2 parameters (title,message)
messagebox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')
#yes no message box, yes returns true value, no returns false
print(messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?'))

#file dialog method to browse
from tkinter import filedialog
#create file dialog, will return an io object
filename = filedialog.askopenfile()
#accesses the path to the file that user selected
print(filename.name)

#import colorchooser module
from tkinter import colorchooser
#define hex value as a string, will return the value of the
print(colorchooser.askcolor(initialcolor = "#FFFFFF"))
