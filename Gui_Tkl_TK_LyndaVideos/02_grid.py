#!/usr/bin/python3
# grid.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#creating labels, children of the root label
#config the row and column methods for each label
ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew')
#sticky configs the blue lavel to the stick to the right position of the grid area
#nesw sets labels to expand in all directiions to fill their cells
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew')
#pad x and pad y adds external padding 10 pixels
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
#ipad add internal padding 25 pixels around x and 25 around y
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)

#config weight on the parent widget and set to 1
#weight property tells the row or column how much it should grow relative to the other rows/cols to fill the space crated when the parent
#widget is resized
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

root.mainloop()
