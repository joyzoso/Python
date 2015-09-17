#!/usr/bin/python3
# mouse.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

#mouse press function
def mouse_press(event):
    global prev
    #printing values to the console
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num)) 
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    #gives you the coordinates related to the entire screen
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}\n'.format(event.y_root))
    prev = event

#create draw method and passing in event
def draw(event):
    global prev
    #track previous and current location of the mouse, line is set to width of 5
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event
    
root = Tk()

#creating canvas object, child of the root 
canvas = Canvas(root, width = 640, height = 480, 
                background = 'white')
#call pack method to place it on the window
canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
