from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import webbrowser





class webGen:

    def __init__(self, master):

        master.title('WebGen')
        #master.resizeable(False, False)
        master.configure(background = '#A36666')

        self.style = ttk.Style()

        self.style.configure('TFrame', background = 'Blue')
        self.style.configure ('TButton', background = '#A36666')
        self.style.configure ('TLabel', background = 'Grey', font = ('Arial', 11))
        self.style.configure ('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = "Website Generator", style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("Enter the text into the "
                  "field below \n to create your webpage!")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()


     
        ttk.Label(self.frame_content, text = 'Text').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.text_comments = Text(self.frame_content, width = 50, height = 5, font = ('Arial', 10))
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
    
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 2, column = 1, padx = 5, sticky = 'ne')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 2, column = 0, padx = 5, sticky = 'ne')
    
           
    def submit(self): #prints to shell, but not to html page
        print('WebPage Text: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = "WOW!", message = "way to go, web developer!!")


    
    def clear (self):
        self.text_comments.delete(1.0, 'end')


        #how do I link this to the submit?
        html = '<html><body>Stay tuned for our amazing summer sale!</body></html>'
        path = os.path.abspath('summersale.html')
        url = 'file://' + path

        with open(path, 'w') as f:
            f.write(html)
        webbrowser.open(url)





def main():            
    
    root = Tk()
    wg = webGen(root)
    root.mainloop()
    
if __name__ == "__main__": main()




