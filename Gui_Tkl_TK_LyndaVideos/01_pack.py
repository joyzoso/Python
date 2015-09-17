#!/usr/bin/python3
# pack.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#create basic label, child of the root label and set back to yellow
#pack manager allows to actually display on the window, packs
ttk.Label(root, text = 'Hello, Tkinter!',
          #side method changes and will be packed against the left side
          #anchor property passes cardinal props (n, e, s, w)
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          #pad props addes external padding on the outside of the widget
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
label = ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green')
#adding internal padding to the widget
label.pack(side = LEFT, ipadx = 10, ipady = 10)
print(label)

#return list of all widgets within a parent widget, useful for conifguring to use methods
for widget in root.pack_slaves():
    #tells widget to fill in both x and y directions as well as when expanding
    widget.pack_configure(fill = BOTH, expand = True)
    #prints dict containing the properties for the widget in the pack manager
    print(widget.pack_info())

#calling the pack forget method on the label itself - specifically the green label
label.pack_forget()

root.mainloop()
