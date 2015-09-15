#!/usr/bin/python3
# menu.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#should always include this to avoid tearoff
root.option_add('*tearOff', False)
#creating menubar
menubar = Menu(root)
#adding it to the root 
root.config(menu = menubar)
#adding new menu items
file = Menu(menubar)
edit = Menu(menubar)
#_because of keyword
help_ = Menu(menubar)

#adds items to the menubar and labels them
menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

#add commands to the file
#lambda is a print function
file.add_command(label = 'New', command = lambda: print('New File'))
#adds a line under the new command
file.add_separator()
#adding 2 more commands
file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
file.add_command(label = 'Save', command = lambda: print('Saving File...'))

#adds the shortcut next to the new command (does not actually bind yet, just display)
file.entryconfig('New', accelerator = 'Ctrl+N')
#subsample shrinks it down
logo = PhotoImage(file = 'python_logo.gif').subsample(10, 10)
#places logo to the left of the text
file.entryconfig('Open...', image = logo, compound = 'left')
#enables or disables state 
file.entryconfig('Open...', state = 'disabled')

#deleting a command
file.delete('Save')
#create a new menu object which is a child of the menu
save = Menu(file)
file.add_cascade(menu = save, label = 'Save')
#add commands to the save submenu
save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
save.add_command(label = 'Save All', command = lambda: print('Saving All...'))

#create variable called choice
choice = IntVar()
#add buttons with the rb method and label it, use the var and the value
edit.add_radiobutton(label = 'One', variable = choice, value = 1)
edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit.add_radiobutton(label = 'Three', variable = choice, value = 3)
#drawing a menu on the screen with the file (creates a pop up menu)
file.post(400, 300)

root.mainloop()
