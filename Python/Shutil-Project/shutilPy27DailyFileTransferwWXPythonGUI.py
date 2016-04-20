import wx
import os
import wx.lib.filebrowsebutton
import time
import datetime
import os.path
import shutil
import subprocess

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        btnSource = wx.Button(panel,label="Browse...",pos=(10,30),size=(120,30))
        btnDestination = wx.Button(panel,label="Browse...",pos=(10,120),size=(120,30))
        btnSubmit = wx.Button(panel,label="Check Files",pos=(280,190),size=(120,30))
        btnSource.Bind(wx.EVT_BUTTON, lambda event:  self.openFile(self.txtSrc))
        btnDestination.Bind(wx.EVT_BUTTON, lambda event:  self.openFile(self.txtDst))
        btnSubmit.Bind(wx.EVT_BUTTON, self.OnButton2)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()

        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')
        fileButton.AppendItem(exitItem)

        menuBar.Append(fileButton, 'File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        self.txtSrc = wx.TextCtrl(panel, size=(250, 27), pos =(150,30)) #Passing in variable
        self.txtDst = wx.TextCtrl(panel, size=(250, 27), pos = (150,120)) #Passing in variable
        
        lblSrc = wx.StaticText(panel, -1, "Source Folder:",(10,10))
        lblDst = wx.StaticText(panel, -1, "Destination Folder:",(10,100)) 

        self.SetTitle('Daily File Transfer Interface')
        self.Show(True)

        

    def openFile(self,out):
        openD = wx.DirDialog(self,"Choose a directory:",style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)
        if openD.ShowModal() == wx.ID_OK:
            out.SetValue(openD.GetPath())
            x = openD.GetPath()
        openD.Destroy()

    def OnButton2(self, event):
        src = self.txtSrc.GetValue() #Passing in variable
        dst = self.txtDst.GetValue() #Passing in variable
        for files in os.listdir(src):
            # Iterate through the source to analyze all 'potential files' to be copied to destination where
            # they will be stored until automated transfer to home office can occur.
            if files.endswith(".txt"):
                # limit by text file.
                source = (os.path.join(src,files))
                destination = (os.path.join(dst,files))
                mtime = (os.path.getmtime(source))
                z = time.time() - mtime
                # Current time per system less time since the file was last modified/created (in seconds).
                    
                _24hrsAgo = time.time() - (24 *60 *60)
                # Exactly 24 hours ago per system time as the script is ran.
                last24hrs = time.time() - _24hrsAgo
                # provides us with the static point in time to compare with how long it has been since each file was
                # last modified/created.
                    
                if z < last24hrs:
                    # Files are only copied from the source folder to the destination folder if they are text files
                    # created or modified within the last 24 hours.  Tested - If script executed multiple times, files that
                    # meet the parameters to be copied, these files will be overwritten in the destination folder so that the
                    # latest version/edit is copied.
                    print('File Detected: {}'.format(files))
                    print('Moved File to: {}'.format(destination))
                    shutil.move(source,destination)
                    # Apparently shutil.copy will only copy a file, it will not cut it and move it.
                    # shutil.move is the correct syntax to cut and move it.



    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None, wx.ID_ANY, "Check for newly created & modified files", size=(420,300), style=wx.SYSTEM_MENU | \
                wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.CAPTION)
    app.MainLoop()

main()
