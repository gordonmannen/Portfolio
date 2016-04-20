import wx
import os
import time
import datetime as dt
import os.path
import shutil
import subprocess
import sqlite3




class Frame(wx.Frame):
    
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(600,300))

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
        lblLastcheck = wx.StaticText(panel, -1, "Last Time Files Checked:",(10,190))

        self.SetTitle("Check for newly created & modified files")
        self.Show(True)
        
        # Create database
        conn = sqlite3.connect('dailyFileTransfer.db')
        c = conn.cursor()

        # Create the new and improved database table
        # we will only need to actually record one thing, the Epoch value since last the last check
        c.execute('''
                    CREATE TABLE IF NOT EXISTS dailyFileTransfer(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    time REAL	NOT NULL
                  );''')
        c.execute("SELECT COUNT (*) FROM dailyFileTransfer") #query to see if this is the first time running app
        rowCount = c.fetchone()[0] #we will receive an error when the database has no data
        # IE: first ran after initial db creation. So we will error trap to prevent a crash
        if rowCount < 1: # So if no data, we need to add the first date to prevent any errors.
            print("No record found, updating database with missing data")
            now = time.time()
            print("time.time() is: {}".format(now))
            c.execute("INSERT INTO dailyFileTransfer (time) VALUES (?)", [now])
            conn.commit()
        c.execute('SELECT max(id) FROM dailyFileTransfer')
        lastID = c.fetchall()[0]
        lastID = lastID[0]
        print("lastID is: {}".format(lastID))
        c.execute('SELECT time FROM dailyFileTransfer WHERE ID = (?)', [lastID])
        lastDate = c.fetchall()[0]
        print("c.fetchall()[0] is:{}".format(lastDate))
        lastDate = lastDate[0]
        lastDate = dt.datetime.fromtimestamp(lastDate).strftime('%m/%d/%Y %H:%M:%S')
        print("lastDate = c.fetchone()[0]: {}".format(lastDate))
        lblLastcheck.SetLabel(lastDate)
        conn.commit()
        conn.close()

    def openFile(self,out):
        openD = wx.DirDialog(self,"Choose a directory:",style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)
        if openD.ShowModal() == wx.ID_OK:
            out.SetValue(openD.GetPath())
            x = openD.GetPath()
        openD.Destroy()

    def OnButton2(self, event):
        src = self.txtSrc.GetValue() #Passing in variable
        dst = self.txtDst.GetValue() #Passing in variable
        a = ("\n********************(File Check Complete )***********************")
        b = ("*****************************************************************")
        conn = sqlite3.connect('dailyFileTransfer.db')
        c = conn.cursor()
        c.execute('SELECT max(id) FROM dailyFileTransfer')
        lastID = c.fetchall()[0]
        lastID = lastID[0]
        print("The lastID is: {}".format(lastID))
        c.execute('SELECT COUNT (*) FROM dailyFileTransfer')
        rowCount = c.fetchall()[0]
        rowCount = rowCount[0]
        print("The rowCount is: {}".format(rowCount))
        c.close()
        
        # Iterate through the source to analyze all 'potential files' to be copied to destination where
        # they will be stored until automated transfer to home office can occur.
        count = 0
        for files in os.listdir(src):
            if files.endswith(".txt"): # filter for text files
                source = (os.path.join(src,files))
                destination = (os.path.join(dst,files))
                mtime = (os.path.getmtime(source))
                timeDiff = time.time() - mtime #Difference from time of file creation or modification until current time 
                _24hrsAgo = time.time() - (24 *60 *60) #Epoch time for a 24hr period is 86400 seconds
                last24hrs = time.time() - _24hrsAgo #Seconds that have occurred within the last 24 hr period
                if timeDiff < last24hrs: #Seconds that have passed since file creation or modification from last 24 hrs
                    count = count + 1
                    print('File detected: {}'.format(files))
                    print('File moved to: {}'.format(destination))
                    shutil.move(source,destination) #Move the qualified files into the destination directory
        if (count > 1):
            print(a)
            print("{} files have been moved into their destination folder...".format(count))
            print(b)
        elif (count == 1):
            print(a)
            print("1 file has been moved into the destination folder...")
            print(b)
        else:
            print(a)
            print("There are no more files to be moved at this time.")
            print(b)
        self.updateDB()
                    
    def updateDB(self):
        # Insert timestamp of current check into the database
        now = time.time()
        conn = sqlite3.connect('dailyFileTransfer.db')
        c = conn.cursor()
        c.execute('SELECT COUNT (*) FROM dailyFileTransfer')
        rowCount = c.fetchall()[0]
        rowCount = rowCount[0]
        print("Current rowCount in the database is: {}".format(rowCount))
        rowCount = (rowCount + 1)
        print("Next rowCount in the database is: {}".format(rowCount))
        c.execute("INSERT INTO dailyFileTransfer (time) VALUES (?)", [now])
        conn.commit()
        conn.close()

    def Quit(self, e):
        self.Close()


def main():
    app = wx.App()
    frame = Frame("Check for newly created & modified files")
    frame.Show()
    app.MainLoop()

if __name__ == "__main__": main()    
