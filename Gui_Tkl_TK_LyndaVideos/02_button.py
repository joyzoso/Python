#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()
#calling the themed button constructor, passing it master and parameter text
button = ttk.Button(root, text = "Click Me")
#calling geometry method
button.pack()

#create a function to execute when pressed
def callback():
    print('Clicked!')

#configure command property to tell it to execute command whenever it is clicked
button.config(command = callback)
#simulate a button click
button.invoke()

#method which determines if it is active or not
button.state(['disabled'])
print(button.instate(['disabled']))
#check the current state of a button (is my button in this state?)
button.state(['!disabled'])
print(button.instate(['!disabled']))

#create image with photoimag constructor
logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
#config method on button to set the image to the logo and places to the left
button.config(image = logo, compound = LEFT)
#another method to resize (every xth and yth pixel in parameters to make smaller image)
small_logo = logo.subsample(5, 5)
#configs button to use the smaller logo
button.config(image = small_logo)

root.mainloop()
