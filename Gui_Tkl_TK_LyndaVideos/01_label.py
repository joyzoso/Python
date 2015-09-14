#!/usr/bin/python3
# label.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#label constructor method, creates the widget object
label = ttk.Label(root, text = "Hello, Tkinter!")
#geometry manager
label.pack()
#changes the text
label.config(text = 'Howdy, Joy!')
#changes the text again in real time
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
#sets number of pixels for text to wrap around to avoid a long long line of text
label.config(wraplength = 150)
#default to left, so making it center and needs to be CAPS
label.config(justify = CENTER)
#another property for back and for colors
label.config(foreground = 'blue', background = 'yellow')
#font property
label.config(font = ('Courier', 18, 'bold'))
#changing the text back to before
label.config(text = 'Howdy, Joy!')

#create a photoimage class
logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
label.config(image = logo)
#configure the image property and replaces the initial text
label.config(compound = 'text')
#displays text in center of image
label.config(compound = 'center')
#displays text to left of image
label.config(compound = 'left')

#saving a reference to logo inside the image variable to avoid garbage collection
label.img = logo
#configuring to use this image
label.config(image = label.img)

root.mainloop()
