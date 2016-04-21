# Using SQLite3 store pre-made content for
# creating web pages and display the choices
# in the GUI so the user can select their choice.

import tkinter as tk
from tkinter import *
import webbrowser
import sqlite3

#Create HTML content database
db = sqlite3.connect('htmlContent.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS htmlContent(id INTEGER PRIMARY KEY, body TEXT)''')
db.commit()

# Enter content into the dB and add to list
def addRecord():
    body_i = source.get()
    con = sqlite3.connect('htmlContent.db')
    with con:
        cursor = con.cursor()
        cursor.execute('''INSERT INTO htmlContent(body) VALUES(?)''', (body_i,))
        lis = cursor.execute('''SELECT body FROM htmlContent''')
        for item in lis:
            list.insert(END, item)

        con.commit()
    print("Record added")
    con.close()

# Pull from list item to Entry box
def pullToEntry(event):
    index = list.curselection()[0]
    seltext = list.get(index)
    webgenEntry.delete(0, 50)
    webgenEntry.insert(0, seltext)

# Bind the selection to Entry box   
def bindToEntry(event):
    try:
        index = list.curselection()[0]
        list.delete(index)
    except IndexError:
        index = tk.END
    list.insert(index, webgenEntry.get())

# Delete from list    
def deleteListItem():
    try:
        index = list.curselection()[0]
        list.delete(index)
    except IndexError:
        pass

# Display all records from the dB in a list
def fetchRecord():
    cont = sqlite3.connect('htmlContent.db')
    with cont:
        cursort = cont.cursor()
        list_loadr = cursort.execute('''SELECT body FROM htmlContent''')
        list_load = list_loadr.fetchall()
        for item in list_load:
            list.insert(tk.END, item)
            
        cont.commit()
        
# Opens a web browser window with the chosen content, works with
# whatever content is currently listed in the text entry box.
def openBrowser():
    f = open('index.html','w')
    text = source.get()
    message = "<html><head></head><body><p>%s</p></body></html>" % text
    f.write(message)
    f.close()
    webbrowser.open_new_tab('index.html')

root = tk.Tk()

root.title("Web Page Generator")

source = tk.StringVar()


list = tk.Listbox(root, width=50, height=6)
list.grid(row=0, column=0)


# Scrollbar for list
yscroll = tk.Scrollbar(command=list.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
list.configure(yscrollcommand=yscroll.set)
 

webgenEntry = tk.Entry(root, textvariable=source, width=50)
webgenEntry.insert(0, 'Click Fetch List, then click on item in list')
webgenEntry.grid(row=1, column=0)

webgenEntry.bind('<Return>', bindToEntry)
webgenEntry.bind('<Double-1>', bindToEntry)

fetchBtn = tk.Button(root, text='Fetch List', command=fetchRecord)
fetchBtn.grid(row=2, column=0, sticky=tk.W)

openBtn = tk.Button(root, text='Open Browser', command=openBrowser)
openBtn.grid(row=3, column=0, sticky=tk.W)

addBtn = tk.Button(root, text='Add Content', command=addRecord)
addBtn.grid(row=2, column=0, sticky=tk.E)

deleteBtn = tk.Button(root, text='Delete List Item', command=deleteListItem)
deleteBtn.grid(row=3, column=0, sticky=tk.E)
 

list.bind('<ButtonRelease-1>', pullToEntry)
 
root.mainloop()