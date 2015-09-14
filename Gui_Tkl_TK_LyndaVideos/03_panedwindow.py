#!/usr/bin/python3
# panedwindow.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#panedwindow construct method with 2 parameters, one being the root
panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
#pack manager which will expand entire space
panedwindow.pack(fill = BOTH, expand = True)

#create frames to add to the window, make it a child of the paned window
frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
#second frame created, also child of the paned window
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
#add frames to the paned window. First parameter is frame 1 and second is weight
panedwindow.add(frame1, weight = 1)
#expands proportinately 4 times than frame 1
panedwindow.add(frame2, weight = 4)

#create a 3rd, another child
frame3 = ttk.Frame(panedwindow, width = 50, height = 50, relief = SUNKEN)
#similar to add method and was inserted between 1 and 2 frames
panedwindow.insert(1, frame3)
#removes a window from the frame. #does not destroy, just hides it.
panedwindow.forget(1)

root.mainloop()
