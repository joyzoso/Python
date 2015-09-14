#!/usr/bin/python3
# progressbar_scale.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#call ttk progbar construct method and config 2 properties (orient and len)
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()


progressbar.config(mode = 'indeterminate')
#turns on the method indeterminately
progressbar.start()
#stops the bar and moves to the left
progressbar.stop()

#config mode propery to determine 
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
#manually setting values
progressbar.config(value = 8.0)
#step fun without any parameters 
progressbar.step()
#steps with 5
progressbar.step(5)

#configured to update itself automatically using the value from a variable
value = DoubleVar()
#configs the variable property to be that value variable
progressbar.config(variable = value)

#using the themed scale constuctor with an orient, length, variable and from params)
scale = ttk.Scale(root, orient = HORIZONTAL,
		  length = 400, variable = value,
		  from_ = 0.0, to = 11.0)

scale.pack()
#programmatically changing the scales
scale.set(4.2)
#programmatically retrieve the value of the scale
print(scale.get())

root.mainloop()
