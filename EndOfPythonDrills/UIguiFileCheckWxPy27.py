import wx
import Tkinter

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()
        editButton = wx.Menu()
        
        exitItem = fileButton.Append(wx.ID_EXIT, 'Check', 'checking files...')
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome User', 'Joy')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()
        

    
        chooseOneBox = wx.SingleChoiceDialog(None, 'Choose the folder for files you wish to check',
                                             'Browse for Folders',
                                             ['Folder A', 'Folder B', 'Folder C', 'Folder D'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            folder = chooseOneBox.GetStringSelection()

            
        wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))

        aweText = wx.StaticText(panel, -1, "You chose Folder...", (3,3))
        aweText.SetForegroundColour('black')
        aweText.SetBackgroundColour('white')
        
        rlyAweText = wx.StaticText(panel, -1, "Choose 'file', then 'check' to execute checking process ", (3, 30))
        rlyAweText.SetForegroundColour(folder)
        rlyAweText.SetBackgroundColour('white')


        chooseOneBox = wx.SingleChoiceDialog(None, 'Choose the folder to move the files',
                                             'Browse for Folders',
                                             ['Folder E', 'Folder F', 'Folder G', 'Folder H'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            folder = chooseOneBox.GetStringSelection()

            
        wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))                
        
        self.SetTitle('Welcome '+userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()


main()
    

#need to include code and bind event that will exectute file check process
#need to fix file-check as it currently exits gui


 
