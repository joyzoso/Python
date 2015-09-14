#!/usr/bin/python3
# toplevel.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *      

#top level windows are not part of the tk themed set    
root = Tk()

#create a second top level window which is a child of the original root window
window = Toplevel(root)
#using title method to differntiate windows
window.title('New Window')

#control how windows are placed on the screen
window.lower()
#helps to control orders
window.lift(root)

#expands window to max size
window.state('zoomed')
#hides window
window.state('withdrawn')
#minimizes window 
window.state('iconic')
#setting back to normal
window.state('normal')
#find the current state
print(window.state())
window.state('normal')

#shortcut methods to minimize and normalize
window.iconify()
window.deiconify()

#default is 200 X 200
#geometry method takes width, height, x and y)
window.geometry('640x480+50+100')
print(window.geometry())
#preventing user from resizing using booleans as parameters in x and y directions
window.resizable(False, False)
#limiting by how much it can be sized
window.maxsize(640, 480)
window.minsize(200, 200)
#setting it back to be allowed to be resized
window.resizable(True, True)

#programmatically closing the window by calling destroy method
#used to destroy all child widgets and top level
root.destroy()

root.mainloop()
