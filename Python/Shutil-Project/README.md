### Shutil Project
***

This project began with a simple automated file transfer, and then I added additional functionality from there.

Initially it is a simple automated file transfer using the shutil module with Python 2.7 in IDLE.  The program checks a particular source folder and transfers any files, in this case limited to text files, to a destination folder.  In the process the program will list the files in the source folder and the associated file path, and a list of the files in the destination folder following the execution of the file transfer.

The next step was to implement aspects of the datetime module so when the program is executed it checks that same folder and the files within and determines if the applicable files have been modified or created within the last twenty-four hours.  If they have it sends a copy of the files meeting those conditions to the destination folder.  It is not a simple file transfer like the previous iteration of the program, shutil.copy rather than shutil.move.

I wanted to implement a UI so I imported the wx module to create a 'Daily File Transfer Interface' that allows the user to browse and manually select their source and destination folders, the program still limits the files that will be moved to text files that have been created or modified within the last twenty-four hours.  I went back to shutil.move as I felt like it would be easier for a user to keep track of which files were moved and whether or not they were working with the latest version of a particular file under that scenario.

The final change that I wanted to implement was introducing interaction with a database using SQLite so a record of when the last "file transfer" was performed could be stored and display that information in the UI for the user.  This version of the program again uses the shutil.move and a slightly modified version of the previous wx UI.  When the process is complete a display message is provided to indicate whether or not files were moved and if so, how many were moved.  Also, if files were moved it reports their new file paths.

Also, to make the program more flexible, I made sure that it could run in Python 2.7 as well as Python 3.5.1 in their respective versions of IDLE and as I have Python 3.5.1 setup in my installation of Visual Studio, I wanted to make sure the Python 3.5.1 file would execute from within Visual Studio.




 
 
Return to [portfolio](../../../../) 
