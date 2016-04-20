import os
import shutil




sourcepath='C:\Folder A'
source = os.listdir(sourcepath)
print(os.listdir(sourcepath))

destinationpath='C:\Folder B'
for files in source:
    if files.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
        print(os.path.join(sourcepath,files))
        

print(os.listdir(destinationpath))

