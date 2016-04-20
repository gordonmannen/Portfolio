import os
import shutil




sourcepath='E:\GPMDocuments\CurrentProjectCSE-RES\TheTechAcademy\Python Course\Python Step 66 - ShutilDrill\Folder A'
source = os.listdir(sourcepath)
print(os.listdir(sourcepath))

destinationpath='E:\GPMDocuments\CurrentProjectCSE-RES\TheTechAcademy\Python Course\Python Step 66 - ShutilDrill\Folder B'
for files in source:
    if files.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
        print(os.path.join(sourcepath,files))
        

print(os.listdir(destinationpath))

