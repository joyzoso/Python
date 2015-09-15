#!/usr/bin/python3
# canvas.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#canvas constructor method
canvas = Canvas(root)
#puts the canvas in the window
canvas.pack()
#specify specs
canvas.config(width = 640, height = 480)

#create line variable, x1, y1, x2, y2 and capture the id using variable to make changes
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
#item config method
canvas.itemconfigure(line, fill = 'green')
print(canvas.coords(line))
#can pass in coordinates to the line
canvas.coords(line, 0, 0, 320, 240, 640, 0)

#config option that smooths the lines
canvas.itemconfigure(line, smooth = True)
#property that draws the line using 5 steps
canvas.itemconfigure(line, splinesteps = 5)
canvas.itemconfigure(line, splinesteps = 100)
#can delete the line
canvas.delete(line)

#rect method taking 4 coordinates and storing it to a variable
rect = canvas.create_rectangle(160, 120, 480, 360)
#pass in parameter to be filled
canvas.itemconfigure(rect, fill = 'yellow')
#oval method
oval = canvas.create_oval(160, 120, 480, 360)
#
arc = canvas.create_arc(160, 1, 480, 240)
#creats an arc with a green fill that extends 180 degrees
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
#create polygon method and passing coordinates to define the polygon
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
#adding text to the canvas
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

#create an image object using the photoimage constructor method and passing the path
logo = PhotoImage(file = 'python_logo.gif') # Change path as needed
#use the canvas create image method to create the image and pass the coord
image = canvas.create_image(320, 240, image = logo)

#using lift method to raise the text above image and top
canvas.lift(text)
#lowers it down in the stack
canvas.lower(image)
#additional parameter to say we just want to lower to just below the text object
canvas.lower(image, text)

#create a button and make it a chold of the canvas
button = Button(canvas, text = 'Click Me')
#set coordinates to where you want button
canvas.create_window(320, 60, window = button)

#creating tags allows referencing by using ID's (custom identifiers)
#add a tag to specify the rect object that is it a shape
canvas.itemconfigure(rect, tags = ('shape'))
#adding two tags that it is shape and round (can have multiple tags)
canvas.itemconfigure(oval, tags = ('shape', 'round'))
#changes both rect and oval to grey
canvas.itemconfigure('shape', fill = 'grey')
#returns all that is associated with that tag
print(canvas.gettags(oval))

root.mainloop()
