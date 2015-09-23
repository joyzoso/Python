import os
import shutil
import time

dira = "C:\Users\student\Desktop\source" #source
dirb = "C:\Users\student\Desktop\updated" #updated


#creates a list of files in dira and sees if a new file is added
files = [file for file in os.listdir(dira)if os.path.isfile(os.path.join(dira,file))]
#if not the already existing file in dira, then copy and add to dir b
for file in files:
    if not os.path.exists(os.path.join(dirb, file)):
        shutil.copy(os.path.join(dira, file),dirb)

#--------------------------------------------------------------------------------#        
#here I am saying if the modified time is less than 24 hours then move to dir b
#for file in files:
#    if time.ctime(os.path.getmtime(file) < 24):
#        shutil.move(os.path.join(dira, file),dirb)
#--------------------------------------------------------------------------------#


#don't think this is executing properly as it is copying each file each time run script
#how can I just copy and move the one modified file that occurs
for file in files:
    if os.path.getmtime(dira) != os.path.getmtime(dirb):
        shutil.copy(os.path.join(dira, file),dirb) 
        
#also need to add an execution that does this once a day
        
#printing list of files in dirb
print os.listdir(dirb)


