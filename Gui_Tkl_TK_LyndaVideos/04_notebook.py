#!/usr/bin/python3
# notebook.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#using notebook construct to create and passing parent
notebook = ttk.Notebook(root)
#using geometry method
notebook.pack()

#creating frame and is a child of the notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
#add the frames to the notebook object
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')
#calling a button constuct and using pack to add it to frame 1
ttk.Button(frame1, text = 'Click Me').pack()


frame3 = ttk.Frame(notebook)
#calling insert method on notebook with 3 parameters
notebook.insert(1, frame3, text = 'Three')
#remove from notebook
notebook.forget(1)
#adding it back to the notebook
notebook.add(frame3, text = 'Three')

#see which tab is selected by the user
print(notebook.select())
#gives ID of the widget and converts it to which tab is selected
print(notebook.index(notebook.select()))
#will switch it over to the 2nd tab
notebook.select(2)

#configs tab and changes propert to disabed and greys it out
notebook.tab(1, state = 'disabled')
#hides it, but still exists
notebook.tab(1, state = 'hidden')
#returns back to normal state
notebook.tab(1, state = 'normal')
#check current text property
notebook.tab(1, 'text')
#check the properties
notebook.tab(1)

root.mainloop()
