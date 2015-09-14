#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com


#import tkinter (* imports all funcs and vars from the the base Tkinter package and allow to directly call them by name)
from tkinter import *
#import the themed TK widgets (sep module) and parf of the Tkinter package
from tkinter import ttk

#instatiate the TK class and calling the method without any arguments and assigning it the var 'root'
#Each instance of the TK class will have its own associated Tcl interpreter.
root = Tk()

#call the ttk.button method (always parent widget in first parameter and then can use 0 or more additional parameters)
button = ttk.Button(root, text = 'Click Me')
#call pack method on button object.
button.pack()

#returns values
print(button['text'])
button['text'] = 'Press Me'
#pass in a new valu
button.config(text = 'Push Me')
#views all available properties for a widget object by calling it without any paramters
#This will retrun a dict with all properites that are avail for the obj and current values
#values are stored in related tuples
print(button.config())

#tkinter creates the widget name as a rand int and appends it to the name of the wigets parent
#here the number 450.. was generated as a unique identifier for the button, and it was appended tp the name of the root window, which is the button's parent.
print(str(button))
#this will return '.' a simple period which is the default name for the top level window object
print(str(root))

#creating a label with the parent, root, specifying the property of text to say hello tkinter, and pack method.
ttk.Label(root, text ='Hello, Tkinter!').pack()

# mainloop() add
root.mainloop()
