#!/usr/bin/python3
# text.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *      

#create top level window    
root = Tk()

#create text box
text = Text(root, width = 40, height = 10)
text.pack()
#wraps text and ends at the nearst word
text.config(wrap = 'word')

#1.0 would be the beginning of the text box, end refers to the last character of the text box
#which will return the entire contents of the text box
print(text.get('1.0', 'end'))
#after the last character in line 1
print(text.get('1.0', '1.end'))
#inserting, deleting and replacing by indexes that are passed
text.insert('1.0 + 2 lines', 'Inserted message')
text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')
text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line.')

#text config method to set the states
text.config(state = 'disabled')
text.delete('1.0', 'end')
#setting the state back to normal
text.config(state = 'normal')


text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background = 'yellow')
text.tag_remove('my_tag', '1.1', '1.3')
print(text.tag_ranges('my_tag'))
print(text.tag_names())
text.replace('my_tag.first', 'my_tag.last', 'That was')
text.tag_delete('my_tag')

#marks specify a single position which exist betwen two characters
text.mark_names()
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
#gravity method either left or right to see where the mark will follow
text.mark_gravity('my_mark', 'right')
#removes mark
text.mark_unset('my_mark')

image = PhotoImage(file = 'python_logo.gif').subsample(5, 5) # Change path as needed
text.image_create('insert', image = image)
text.image_create('insert', image = image)

#creating a button as a child of the text widget
button = Button(text, text = 'Click Me')
#passing the index and window property
text.window_create('insert', window = button)

root.mainloop()
