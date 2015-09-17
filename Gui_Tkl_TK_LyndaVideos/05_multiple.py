#!/usr/bin/python3
# multiple.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#create 2 label widgets, child of the root
label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
#add those to the window with pack command
label1.pack()
label2.pack()

#use bind to add a message and using mouse event and execute lambda function
label1.bind('<ButtonPress>', lambda e: print('<BP> Label'))
#button one is pressed specifically
label1.bind('<1>', lambda e: print('<1> Label'))

root.bind('<1>', lambda e: print('<1> Root'))

#remove previous bindings
label1.unbind('<1>')
label1.unbind('<ButtonPress>')

root.bind_all('<Escape>', lambda e: print('Escape!'))

root.mainloop()
