# Create an HTML document using Python

# Add GUI to enable the user to set the body of the text.
# Should have a submit button for initiating the process
# of making the new web page/naviagiting to the new page.

import sys
import webbrowser
from tkinter import *

def retrieve_input():
    _input = text1.get("1.0",END) # input is reserved so need the _ or cannot use it as a variable.
    message = ("""
<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>Company Page - Marketing Department</title>
    </head>
    <body>
        <pre>
            <font size="2" face="verdana" color"black">
                """)+_input+("""
            </font>
        </pre>
    </body>
</html>
""")

    if (_input > ' '):
       with open('htmlpage.html', 'w') as tempFile:
           tempFile.write(message)
           tempFile.close()
           url = "htmlpage.html" 
           new = 2
           webbrowser.open(url,new=new)
    else:
        messagebox.showwarning("Empty Text Box Detected!", "You must enter some body text.")

root = Tk()

root.geometry('850x450+200+200')
root.title('Update body of HTML with new content')

text1 = Text(root)
text1.pack()

submitLabel = Label(root,text='Once you are satisfied with the body text, click Submit').pack()
submitButton = Button(root,text="Submit", command=retrieve_input)
submitButton.pack()

mainloop()