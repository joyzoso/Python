#!/usr/bin/python3
# virtual.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#creating entry widget and packing it to top level window
entry = ttk.Entry(root)
entry.pack()

#bind to an event in the entry box
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

#prints the information about this virtual event
print(entry.event_info('<<OddNumber>>'))

#programmatically trigger the event
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

#entry.event_delete('<<OddNumber>>')

root.mainloop()
