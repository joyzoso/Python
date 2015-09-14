#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#using ttk module and checkbutton constructor method
checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
#geometry manager for sizing
checkbutton.pack()

#calling stringvar constructor method and saving it to the variable called spam
spam = StringVar()
#using set method to set the value of the variable
spam.set('SPAM!')
#using get method to check the current value of the variable
print(spam.get())

#setting the variable property to be the name of the variable spam and having an onvalue
checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
                   #check button is not selected well then say boo spam
		   offvalue = 'Boo SPAM!')
print(spam.get())

breakfast = StringVar()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
print(breakfast.get()) # Note: value will be empty if no selection is made

checkbutton.config(textvariable = breakfast)

root.mainloop()
