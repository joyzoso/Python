#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#using tk constructor method
treeview = ttk.Treeview(root)
treeview.pack()
#adding nodes in the tree, first parameter is the parent node, second is position, id is third and 4th is optional)
treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
#end adds at the end
treeview.insert('', 'end', 'item3', text = 'Third Item')

#bring image in
logo = PhotoImage(file = 'C:\\Users\\barron\\Dropbox\\Lynda Courses\\Python GUI Development with Tkinter\\Exercise Files - Current\\03 Widget Classes\\python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)

#change the height property
treeview.config(height = 5)
#item, parent, index (takes item 2 move it under item 1 and place it at the end of the items)
treeview.move('item2', 'item1', 'end')
#by default items are in the closed position, so here we are setting it to open
treeview.item('item1', open = True)
#check the status of the open property
treeview.item('item2', open = True)
print(treeview.item('item1', 'open'))

#detach the node from the tree move
treeview.detach('item3')
#moving back item 3
treeview.move('item3', 'item2', '0')
#completely delete item from the view and cannot be re-added
treeview.delete('item3')

#config columns property and list what you want to include
treeview.configure(column = ('version'))
#config properties of the column (name, width, anchor)
treeview.column('version', width = 50, anchor = 'center')
#similar to above
treeview.column('#0', width = 150)
#pass in the name of the column and what text you want it to be
treeview.heading('version', text = 'Version')
treeview.set('python', 'version', '3.4')
#similar to tag method
treeview.item('python', tags = ('software'))
#once tags are established, can config properties as groups
treeview.tag_configure('software', background = 'yellow')

#define callback func
def callback(event):
    #prints current item that is selected
    print(treeview.selection())

#bind method, passing name of the event that is unique to the treeview, when this occurs
    #will execute callback function
treeview.bind('<<TreeviewSelect>>', callback)

#by default allows multiple items selected at once, but can modify this so one is selected at a time
treeview.config(selectmode = 'browse')
#selection add method will add 'python'
print(treeview.selection_add('python'))
#can programmtically unselect 'python'
print(treeview.selection_remove('python'))
print(treeview.selection_toggle('python'))

root.mainloop()
