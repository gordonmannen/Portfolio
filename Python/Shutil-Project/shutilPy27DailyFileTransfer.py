import time
import datetime
import os
import os.path
import shutil


def daily_scriptcopy():
    sourcepath='C:\Folder A'

    for files in os.listdir(sourcepath):
        # Iterate through the source to analyze all 'potential files' to be copied to destination where
        # they will be stored until automated transfer to home office can occur.
        if files.endswith(".txt"):
            # limit by text file.
            source = 'C:\Folder A\{}'.format(files)
            destinationpath = 'C:\Folder B\{}'.format(files)
            mtime = (os.path.getmtime(source))

            x = time.time() - mtime
            # Current time per system less time since the file was last modified/created (in seconds).
            
            _24hrsAgo = time.time() - (24 *60 *60)
            # Exactly 24 hours ago per system time as the script is ran.
            last24hrs = time.time() - _24hrsAgo
            # provides us with the static point in time to compare with how long it has been since each file was
            # last modified/created.
            
            if x < last24hrs:
                # Files are only copied from the source folder to the destination folder if they are text files
                # created or modified within the last 24 hours.  Tested - If script executed multiple times, files that
                # meet the parameters to be copied, these files will be overwritten in the destination folder so that the
                # latest version/edit is copied.
                print('source: {}'.format(source))
                print('destination: {}'.format(destinationpath))
                shutil.copy(source,destinationpath)

daily_scriptcopy()            


    

