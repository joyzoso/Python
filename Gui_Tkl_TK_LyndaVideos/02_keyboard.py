#!/usr/bin/python3
# keyboard.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

#create keypress handler
def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}\n'.format(event.keycode))

#shortcut function
def shortcut(action):
    print(action)
    
root = Tk()

#bind method on the root window
#creating a shortcut function called copy
#need to include additional variable e to capture the event object.
root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()
