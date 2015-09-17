#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')      
button1.pack()
button2.pack()

#create a style object and store it in a variable calld style
style = ttk.Style()

#lists themes available
print(style.theme_names())
#call with any paramters and see current theme
print(style.theme_use())
#use classic theme                    
style.theme_use('classic')
#return back to vista
style.theme_use('vista')


print(button1.winfo_class())
#using style object and calling config method
style.configure('TButton', foreground = 'blue')
#create custom button style and define new style name
style.configure('Alarm.TButton', foreground = 'orange',
                font = ('Arial', 24, 'bold'))
#inherited all button styles except for those specified
button2.configure(style = 'Alarm.TButton')
#pair of the state of being pressed and then a pair is disabled
style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')])
button2.state(['disabled'])

#gives a list of all the elements with that style
print(style.layout('TButton'))
#see what options are available for each element ie: label to fully customize
print(style.element_options('Button.label'))
#see what values have been configured for the style ie: Tbutton and returns current proprty of that method 
print(style.lookup('TButton', 'foreground'))

root.mainloop()
