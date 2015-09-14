#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com



from tkinter import *
from tkinter import ttk

class HelloApp: 
#init constructor method takes one parameter called master which is the TK widget to use
#as parent of all other widgets in the GUI.    
    def __init__(self, master):
        #label is a child of the master window
        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        #storing a reference to this label
        self.label.grid(row = 0, column = 0, columnspan = 2)

        #if texas button is clicked the command property will be the callback method for texas_hello method
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)
        #if hawaii button is clicked the command property will be the callback method for hawaii_hello method
        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)
    #associated handler methods are self contained
    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

            
def main():            
    #tk constructor method to create a top level TK window named root
    root = Tk()
    #passing root to the helloapp constructor method to use as the master window
    app = HelloApp(root)
    #calling the mainloop method on the top level window to enter into the TK event loop
    root.mainloop()
# detects that the init method is being run as main and will execute the main function    
if __name__ == "__main__": main()
