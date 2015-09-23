from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mebo
from tkinter import filedialog as fidi
import shutil, os
import sqlite3 as sql
import datetime, time




class FTP:

    def __init__(self, master):

        master.title('FTP')
        master.resizable(False, False)
        master.configure(background = '#A36666')
        

        self.style = ttk.Style()
        
        self.style.configure('TFrame', background = '#A36666')
        self.style.configure ('TButton', background = '#A36666')
        self.style.configure ('TLabel', background = '#A36666', font = ('Arial', 11))
        self.style.configure ('Header.TLabel', font = ('Arial', 18, 'bold'))
        

        #HEAD
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        #self.logo = PhotoImage(file = '')#get other pic 75X75
        #ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = "File Transfer Program", style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("Search for a file to open "
                  "then search \n and choose a new destination")).grid(row = 1, column = 1)


        #MAIN
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'File to move').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Destination').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        #ENTRY
        self.file_move = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.file_dest = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        #text widget does not come from the ttk module
        self.text_comments = Text(self.frame_content, width = 50, height = 5, font = ('Arial', 10))
        
        self.file_move.grid(row = 1, column = 0, padx = 5)
        self.file_dest.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        
        #BUTTONS #should self.transfer be self.content?? #can I use invoke() here?
        ttk.Button(self.frame_content, text = 'Search', command = self.search1).grid(row = 2, column = 0, padx = 5, sticky = 'ne')
        ttk.Button(self.frame_content, text = 'Search', command = self.search2).grid(row = 2, column = 1, padx = 5, sticky = 'ne')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 5, column = 0, padx = 5, sticky = 'sw')
        ttk.Button(self.frame_content, text = 'Transfer', command = self.trans).grid(row = 4, column = 1, padx = 5, sticky = 'sw')
        ttk.Button(self.frame_content, text = 'Cancel', command = quit).grid(row = 5, column = 1, padx = 5, sticky = 'sw')


        #EVENTS 
    def trans(self):
        self.drillDatabase() #This may be an issue transferring to DB
        path = self.file_move.get()
        destination = self.file_dest.get()
        #self.inserttrans()
        self.insertfile()
        shutil.copy(path, destination)
        self.clear()
        messagebox.showinfo(title = "FTP", message = "File Transferred!")

        #database
    def drillDatabase(self):
        self.conn = sql.connect('ftpDrill.db')

        self.cc = self.conn.cursor()
        


    def clear(self):
        self.file_move.delete(0, 'end') #deleted from entry_name
        self.file_dest.delete(0, 'end')
        #line 1, character 0
        self.text_comments.delete(1.0, 'end')


    def search1(self):
        move = filedialog.askopenfilename()
        self.file_move.delete(0,'end')
        self.file_move.insert(0,move)

    def search2(self):
        destination = filedialog.askdirectory()
        self.file_dest.delete(0,'end')
        self.file_dest.insert(0,destination)
        


    #def inserttrans(self): #do I need all the time stuff
    #    move= self.file_move.get()
    #    stats=[time.strftime('%Y-%m-%d %H:%M:%S', path.getmtime(os.path.getmtime(move))),
    #          datetime.datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')]
    #    transferID = 0
    #    for i in stats:
    #        ID +=1
    #        self.conn.execute("INSERT INTO fileCheck VALUES(?,?,?,?)", #line 1 character 0 in comment field
    #                       (transferID,i,i,self.text_comments.get(1.0,'end')))
            
        self.conn.commit()



    def insertfile(self):
        move = self.file_move.get()
        destination = self.file_dest.get()
        type = os.path.splitext(self.file_move.get())[1] 
        transferID = 0
        fileID = 0
        self.conn.execute("INSERT INTO transferCheck VALUES(?,?,?,?,?)",
                       (fileID, move, destination, type, transferID))
        
        self.conn.commit()

        
        

    def lasttrans(self): #not sure if this is executing properly
        runtime = time.clock()
        print(runtime)
            

        #EVENT BINDING
        self.trans.bind('<1>', lambda e: self.trans())
        self.clear.bind('<1>', lambda e: self.clear())
        self.search1.bind('<1>', lambda e: self.search1())
        self.search2.bind('<1>', lambda e: self.search2())
            
def main():            
    
    root = Tk()
    ftp = FTP(root)
    root.mainloop()
    
if __name__ == "__main__": main()
