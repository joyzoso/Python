#!/usr/bin/python3
# callback.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

#defining a method called callback
def callback(number):
    print(number)
    
root = Tk()
#lambda keyword creates an anonymous function containing the callback method
#that can be used to configure the command callback
#lambda will point to the callback function passing the correct params for that number
ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()

#starts the event loop
root.mainloop()
